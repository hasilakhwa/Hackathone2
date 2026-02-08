
```markdown
---
name: nextjs-authenticated-api-client
description: Create a reusable API fetch client in Next.js that automatically attaches JWT Bearer token. Use for all backend API calls from frontend.
---

# Next.js Authenticated API Client

## Instructions

1. **Token storage**
   - Use localStorage or cookies (Better Auth usually handles)

2. **Interceptor / wrapper**
   - Create fetch wrapper or axios instance
   - Add Authorization header if token exists

3. **Error handling**
   - Redirect to login on 401
   - Show toast on other errors

## Best Practices
- Use relative URLs (/api/...) or full backend URL from env
- Refresh token logic if implemented later
- Type responses with TypeScript interfaces
- Add loading states in UI

## Example Structure

```ts
// lib/api.ts
import { getSession } from "@better-auth/next";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function apiFetch<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const session = await getSession();
  const token = session?.token; // or however Better Auth exposes JWT

  const headers = {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...options.headers,
  };

  const res = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers,
  });

  if (res.status === 401) {
    // redirect to login or refresh
    window.location.href = "/login";
    throw new Error("Unauthorized");
  }

  if (!res.ok) {
    throw new Error(await res.text());
  }

  return res.json() as Promise<T>;
}

// Usage
export const getTasks = (userId: string) =>
  apiFetch<Task[]>(`/api/${userId}/tasks`);