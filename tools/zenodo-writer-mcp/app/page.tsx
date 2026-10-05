export default function Page() {
  return (
    <main style={{fontFamily:"system-ui",maxWidth:760,margin:"64px auto",padding:"0 20px"}}>
      <h1>Zenodo Writer MCP</h1>
      <p>Private MCP service for controlled Zenodo deposit workflows.</p>
      <ul>
        <li>Zenodo token is read only from server-side environment variables.</li>
        <li>Publishing requires an explicit confirmation string.</li>
        <li>The MCP endpoint is <code>/api/mcp</code>.</li>
      </ul>
    </main>
  );
}
