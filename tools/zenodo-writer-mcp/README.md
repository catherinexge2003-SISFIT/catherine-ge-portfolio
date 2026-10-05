# Zenodo Writer MCP

Private server-side MCP integration for Zenodo deposit workflows.

## Security model

- `ZENODO_TOKEN` is read only from Vercel environment variables.
- The Zenodo token is never stored in GitHub or returned by any tool.
- `ZENODO_API_BASE` is restricted to `https://zenodo.org/api` or `https://sandbox.zenodo.org/api`.
- Remote file ingestion is restricted to `sisfit.cn` and `raw.githubusercontent.com`.
- MCP access is protected by Clerk OAuth; unauthenticated requests are rejected before tool execution.
- Publishing requires the exact confirmation value `PUBLISH_ZENODO_RECORD`.
- Draft deletion requires `DELETE_DRAFT`.

## Environment variables

- `ZENODO_TOKEN` — required; Vercel Sensitive env var.
- `ZENODO_API_BASE` — optional; defaults to `https://zenodo.org/api`.
- `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` — required; Clerk publishable key.
- `CLERK_SECRET_KEY` — required; Vercel Sensitive env var. Never commit it.

## MCP endpoint

`/api/mcp`

OAuth discovery endpoints:

- `/.well-known/oauth-protected-resource/api/mcp`
- `/.well-known/oauth-authorization-server`

Clerk client onboarding is configured for CIMD. Dynamic Client Registration is intentionally disabled.

## Initial verification

Do not create or publish a Zenodo record during connection testing.

1. Connect through Clerk OAuth.
2. `zenodo_health`
3. `list_deposits`

Only after this read-only path passes should a real v0.1 draft be created and a DOI reserved.
