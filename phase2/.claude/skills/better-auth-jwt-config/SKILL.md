
```markdown
---
name: better-auth-jwt-config
description: Configure Better Auth with JWT plugin in Next.js for token issuance and client usage. Use for auth setup on frontend side.
---

# Better Auth + JWT Plugin Setup

## Instructions

1. **Install plugin**
   - Add jwt() to betterAuth plugins

2. **Server config**
   - Export auth with jwt plugin

3. **Client config**
   - Add jwtClient() to createAuthClient

4. **Get token**
   - Use getAccessToken() or similar to retrieve JWT

## Best Practices
- Use same BETTER_AUTH_SECRET in .env for both FE/BE
- Enable key rotation if production
- Handle token expiry in client
- Use secure cookie for session

## Example Structure

```ts
// lib/auth.ts (server)
import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
  plugins: [jwt()],
  // other config: database, email, etc.
});

// api/auth/[...all]/route.ts
import { toNextJsHandler } from "better-auth/next-js";
export const { GET, POST } = toNextJsHandler(auth);

// lib/auth-client.ts (client)
import { createAuthClient } from "better-auth/client";
import { jwtClient } from "better-auth/client/plugins";

export const { signIn, signOut, useSession } = createAuthClient({
  plugins: [jwtClient()],
});