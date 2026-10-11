const clientId =
  "https://zenodo-mcp.sisfit.cn/.well-known/oauth-client/mcp-inspector";

export function GET() {
  return Response.json(
    {
      client_id: clientId,
      client_name: "MCP Inspector",
      redirect_uris: ["http://127.0.0.1:6276/oauth/callback"],
      grant_types: ["authorization_code"],
      response_types: ["code"],
      token_endpoint_auth_method: "none"
    },
    {
      headers: {
        "Cache-Control": "no-store",
        "Content-Type": "application/json"
      }
    }
  );
}
