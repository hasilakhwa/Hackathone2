# Claude Agent Context for Next.js Frontend Development

## Technologies Used
- Next.js 16+ with App Router
- TypeScript
- Tailwind CSS
- Better Auth with JWT plugin
- @better-auth/client
- Framer Motion
- Sonner (for toasts)
- Optional: shadcn/ui components
- FastAPI backend
- NeonDB database
- CORS middleware

## Architecture Patterns
- Next.js App Router directory structure
- Client-side session management with Better Auth
- Centralized API client with authentication token injection
- Component-based UI architecture
- Responsive design with mobile-first approach

## Key Implementation Details
- Authentication routes in app/api/auth/[...all]/route.ts
- Server-side auth configuration in lib/auth.ts
- Client utilities for session management
- Protected routes using Next.js middleware
- API client wrapper in lib/api.ts with JWT token handling
- CORS configuration for cross-origin requests between frontend and backend
- User isolation mechanisms for task data
- Error handling with toast notifications and redirects