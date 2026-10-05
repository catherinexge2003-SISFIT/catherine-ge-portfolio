import { createMcpHandler } from "mcp-handler";
import { z } from "zod";
import {
  createDeposit,
  deleteDeposit,
  getDeposit,
  listDeposits,
  publishDeposit,
  updateDeposit,
  uploadFromUrl
} from "@/lib/zenodo";

export const runtime = "nodejs";

const Creator = z.object({
  name: z.string().min(1).describe('Zenodo creator name, preferably "Family, Given"'),
  affiliation: z.string().optional(),
  orcid: z.string().optional()
});

const Metadata = z.object({
  title: z.string().min(1),
  upload_type: z.enum(["dataset", "software", "publication", "other"]).default("dataset"),
  description: z.string().min(1),
  creators: z.array(Creator).min(1),
  publication_date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).optional(),
  access_right: z.enum(["open", "embargoed", "restricted", "closed"]).default("open"),
  license: z.string().default("cc-by-4.0"),
  version: z.string().optional(),
  keywords: z.array(z.string()).optional(),
  prereserve_doi: z.union([z.boolean(), z.object({ doi: z.string().optional(), recid: z.number().optional() })]).optional()
});

function result(data: unknown) {
  return { content: [{ type: "text" as const, text: JSON.stringify(data, null, 2) }] };
}

const handler = createMcpHandler(
  (server) => {
    server.tool(
      "zenodo_health",
      "Check server configuration without exposing secrets or modifying Zenodo.",
      {},
      async () => result({
        configured: Boolean(process.env.ZENODO_TOKEN),
        apiBase: process.env.ZENODO_API_BASE || "https://zenodo.org/api"
      })
    );

    server.tool(
      "list_deposits",
      "List the authenticated user's Zenodo deposits. Read-only.",
      { status: z.enum(["draft", "published"]).optional() },
      async ({ status }) => {
        const deposits = await listDeposits(status);
        return result(deposits.map((d: any) => ({
          id: d.id,
          title: d.title || d.metadata?.title || "",
          state: d.state,
          submitted: d.submitted,
          doi: d.doi || d.metadata?.prereserve_doi?.doi || null,
          html: d.links?.html || null
        })));
      }
    );

    server.tool(
      "get_draft",
      "Retrieve one Zenodo deposition by numeric ID. Read-only.",
      { id: z.number().int().positive() },
      async ({ id }) => result(await getDeposit(id))
    );

    server.tool(
      "create_draft",
      "Create an unpublished Zenodo draft. This does not publish it.",
      { metadata: Metadata.omit({ prereserve_doi: true }) },
      async ({ metadata }) => result(await createDeposit(metadata))
    );

    server.tool(
      "update_metadata",
      "Replace metadata on an unpublished Zenodo draft. This does not publish it.",
      { id: z.number().int().positive(), metadata: Metadata },
      async ({ id, metadata }) => result(await updateDeposit(id, metadata))
    );

    server.tool(
      "reserve_doi",
      "Reserve a DOI for an unpublished Zenodo draft. The DOI is not registered until publication.",
      { id: z.number().int().positive() },
      async ({ id }) => {
        const current = await getDeposit(id);
        const metadata = { ...(current.metadata || {}), prereserve_doi: true };
        const updated = await updateDeposit(id, metadata);
        return result({
          id: updated.id,
          reserved_doi: updated.metadata?.prereserve_doi?.doi || null,
          state: updated.state,
          submitted: updated.submitted
        });
      }
    );

    server.tool(
      "upload_file_from_url",
      "Upload a public file from sisfit.cn or raw.githubusercontent.com to an unpublished Zenodo draft.",
      {
        id: z.number().int().positive(),
        file_url: z.string().url(),
        filename: z.string().min(1).optional()
      },
      async ({ id, file_url, filename }) => result(await uploadFromUrl(id, file_url, filename))
    );

    server.tool(
      "delete_draft",
      "Delete an unpublished Zenodo draft. Requires the exact confirmation string DELETE_DRAFT.",
      {
        id: z.number().int().positive(),
        confirmation: z.literal("DELETE_DRAFT")
      },
      async ({ id }) => {
        await deleteDeposit(id);
        return result({ deleted: true, id });
      }
    );

    server.tool(
      "publish_deposit",
      "Permanently publish a Zenodo draft and register its DOI. Use only after explicit user approval. Requires the exact confirmation string PUBLISH_ZENODO_RECORD.",
      {
        id: z.number().int().positive(),
        confirmation: z.literal("PUBLISH_ZENODO_RECORD")
      },
      async ({ id }) => result(await publishDeposit(id))
    );
  },
  {},
  { basePath: "/api" }
);

export { handler as GET, handler as POST, handler as DELETE };
