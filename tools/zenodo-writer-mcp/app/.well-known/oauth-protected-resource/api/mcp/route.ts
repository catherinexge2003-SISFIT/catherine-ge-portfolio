import { metadataCorsOptionsRequestHandler } from "@clerk/mcp-tools/next";
import {
  corsHeaders,
  generateClerkProtectedResourceMetadata
} from "@clerk/mcp-tools/server";

function handler(req: Request) {
  const publishableKey = process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY;
  if (!publishableKey) {
    throw new Error("Missing NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY environment variable");
  }

  const metadata = generateClerkProtectedResourceMetadata({
    publishableKey,
    resourceUrl: new URL("/api/mcp", req.url).toString(),
    properties: {
      scopes_supported: ["openid", "profile", "email"]
    }
  });

  return Response.json(metadata, {
    headers: Object.assign(
      {
        "Cache-Control": "max-age=3600",
        "Content-Type": "application/json"
      },
      corsHeaders
    )
  });
}

const corsHandler = metadataCorsOptionsRequestHandler();

export { handler as GET, corsHandler as OPTIONS };
