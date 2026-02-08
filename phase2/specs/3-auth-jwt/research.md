# Research: JWT Authentication Bridge Implementation with Better Auth

## Decision: Use Better Auth for Next.js authentication with JWT plugin

### Rationale:
Based on the user requirements and constitution principles, Better Auth is the optimal choice because:
- Aligns with Technology Stack Adherence principle (Better Auth specified in constitution)
- Provides comprehensive authentication solution with built-in JWT support
- Supports stateless authentication as required by constitution
- Integrates well with Next.js App Router architecture
- Handles user registration/login flows out of the box

### Technical Approach:
- Configure Better Auth server-side with jwt() plugin enabled
- Use BETTER_AUTH_SECRET from environment for token signing/verification
- Implement server-side auth routes in [...all]/route.ts pattern
- Create client-side helpers using better-auth/client with jwtClient plugin

## Decision: Backend JWT Verification Implementation

### Rationale:
Following the constitution's Security-First Design and Stateless Authentication principles:
- Use python-jose or PyJWT for token verification on the backend
- Verify tokens using same BETTER_AUTH_SECRET as frontend
- Implement HS256 algorithm for consistency with Better Auth defaults
- Extract user_id from token claims for user isolation

### Implementation Details:
- Reuse/extend get_current_user dependency from previous specification
- Decode JWT tokens and validate signature integrity
- Extract user_id from token's sub or user_id claim
- Return 401 Unauthorized for invalid/missing/expiration tokens
- Validate token expiration (exp claim)

### Alternatives Considered:
1. Custom JWT implementation vs Better Auth + python-jose:
   - Chose Better Auth + python-jose for security and reliability
   - Custom implementation would be error-prone and non-standard

## Decision: Frontend Token Management Strategy

### Rationale:
Aligns with stateless authentication requirements and best practices:
- Store JWT tokens in secure session cookies via Better Auth
- Use getAccessToken() or session.token pattern for API calls
- Attach Bearer tokens to all protected API requests
- Implement proper token refresh/handling for expired tokens

### Implementation Details:
- Create client-side API fetch wrapper that automatically attaches JWT
- Handle 401 responses gracefully (redirect to login)
- Secure token storage using Better Auth's built-in mechanisms

## Decision: Shared Secret Management

### Rationale:
Following the security and environment management requirements:
- Use BETTER_AUTH_SECRET from .env file on both frontend and backend
- Never hardcode secrets in source code
- Load secrets using load_dotenv on both sides
- Ensure consistency between frontend and backend configuration

### Alternatives Considered:
1. Hardcoded secrets vs environment variables:
   - Environment variables chosen for security and flexibility
   - Hardcoding would violate security principles

## Decision: Project Structure for Authentication

### Rationale:
Following the Modularity & Reusability principle:
- Separate auth configuration for frontend and backend
- Reusable authentication helpers and middleware
- Clear separation of concerns between auth and business logic
- Organize files according to Next.js and FastAPI best practices

### Structure:
- Frontend: frontend/lib/auth.ts (server and client helpers)
- Backend: backend/dependencies/auth.py (update existing auth dependency)
- Shared: .env configuration for shared secrets