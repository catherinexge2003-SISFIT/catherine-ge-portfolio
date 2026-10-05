# Zenodo Writer MCP

Private server-side MCP integration for Zenodo deposit workflows.

## Security model

- `ZENODO_TOKEN` is read only from Vercel environment variables.
- The Zenodo token is never stored in GitHub or returned by any tool.
- `ZENODO_API_BASE` is restricted to `https://zenodo.org/api` or `https://sandbox.zenodo.org/api`.
- Remote file ingestion is restricted to `sisfit.cn` and `raw.githubusercontent.com`.
- Publishing requires the exact confirmation value `PUBLISH_ZENODO_RECORD`.
- Draft deletion requires `DELETE_DRAFT`.

## Environment variables

- `ZENODO_TOKEN` — required; Vercel Sensitive env var.
- `ZENODO_API_BASE` — optional; defaults to `https://zenodo.org/api`.

## MCP endpoint

`/api/mcp`

## Initial verification

Do not publish during connection testing.

1. `zenodo_health`
2. `list_deposits`
3. Create one empty/test draft if needed.
4. Retrieve it with `get_draft`.
5. Delete the test draft with `delete_draft`.

Only after this passes should a real record be created and a DOI reserved.
