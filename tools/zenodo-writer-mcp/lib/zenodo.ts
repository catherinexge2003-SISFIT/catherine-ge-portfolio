const DEFAULT_BASE = "https://zenodo.org/api";

function apiBase(): string {
  const value = (process.env.ZENODO_API_BASE || DEFAULT_BASE).replace(/\/$/, "");
  const url = new URL(value);
  const allowed = new Set(["zenodo.org", "sandbox.zenodo.org"]);
  if (url.protocol !== "https:" || !allowed.has(url.hostname)) {
    throw new Error("ZENODO_API_BASE must be https://zenodo.org/api or https://sandbox.zenodo.org/api");
  }
  return value;
}

function token(): string {
  const value = process.env.ZENODO_TOKEN;
  if (!value) throw new Error("ZENODO_TOKEN is not configured");
  return value;
}

async function parseResponse(res: Response): Promise<any> {
  const text = await res.text();
  const body = text ? (() => { try { return JSON.parse(text); } catch { return text; } })() : null;
  if (!res.ok) {
    const detail = typeof body === "string" ? body : JSON.stringify(body);
    throw new Error(`Zenodo ${res.status} ${res.statusText}: ${detail}`);
  }
  return body;
}

export async function zenodoJson(path: string, init: RequestInit = {}): Promise<any> {
  const headers = new Headers(init.headers);
  headers.set("Authorization", `Bearer ${token()}`);
  if (init.body && !headers.has("Content-Type")) headers.set("Content-Type", "application/json");
  const res = await fetch(`${apiBase()}${path}`, { ...init, headers, cache: "no-store" });
  return parseResponse(res);
}

export async function listDeposits(status?: "draft" | "published"): Promise<any[]> {
  const qs = new URLSearchParams({ sort: "-mostrecent", size: "100" });
  if (status) qs.set("status", status);
  return zenodoJson(`/deposit/depositions?${qs.toString()}`);
}

export async function getDeposit(id: number): Promise<any> {
  return zenodoJson(`/deposit/depositions/${id}`);
}

export async function createDeposit(metadata: Record<string, unknown>): Promise<any> {
  return zenodoJson("/deposit/depositions", {
    method: "POST",
    body: JSON.stringify({ metadata })
  });
}

export async function updateDeposit(id: number, metadata: Record<string, unknown>): Promise<any> {
  return zenodoJson(`/deposit/depositions/${id}`, {
    method: "PUT",
    body: JSON.stringify({ metadata })
  });
}

export async function deleteDeposit(id: number): Promise<void> {
  await zenodoJson(`/deposit/depositions/${id}`, { method: "DELETE" });
}

export async function publishDeposit(id: number): Promise<any> {
  return zenodoJson(`/deposit/depositions/${id}/actions/publish`, { method: "POST" });
}

export async function uploadFromUrl(id: number, fileUrl: string, filename?: string): Promise<any> {
  const source = new URL(fileUrl);
  const allowedHosts = new Set(["sisfit.cn", "www.sisfit.cn", "raw.githubusercontent.com"]);
  if (source.protocol !== "https:" || !allowedHosts.has(source.hostname)) {
    throw new Error("file_url must be HTTPS and hosted on sisfit.cn or raw.githubusercontent.com");
  }

  const sourceRes = await fetch(source.toString(), { cache: "no-store" });
  if (!sourceRes.ok) throw new Error(`Source download failed: ${sourceRes.status} ${sourceRes.statusText}`);
  const bytes = await sourceRes.arrayBuffer();
  if (bytes.byteLength > 95 * 1024 * 1024) throw new Error("File exceeds 95 MB safety limit");

  const name = filename || decodeURIComponent(source.pathname.split("/").filter(Boolean).pop() || "upload.bin");
  const form = new FormData();
  form.append("name", name);
  form.append("file", new Blob([bytes]), name);

  const res = await fetch(`${apiBase()}/deposit/depositions/${id}/files`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token()}` },
    body: form
  });
  return parseResponse(res);
}
