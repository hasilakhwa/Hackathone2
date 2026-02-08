<!-- SYNC IMPACT REPORT:
Version change: N/A -> 1.0.0
Modified principles: None (new constitution)
Added sections: All sections
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->
# AI-Powered Todo Chatbot Constitution

## Core Principles

### Technology Stack Adherence
Strict adherence to provided technology stack: OpenAI ChatKit (Frontend), Python FastAPI (Backend), OpenAI Agents SDK (AI Framework), Official MCP SDK (MCP Server), SQLModel ORM, Neon Serverless PostgreSQL, Better Auth with JWT. All implementations MUST use only these specified technologies without deviation.

### Security-First Design
Enforce user isolation, stateless JWT auth, no cross-user data access, always verify ownership. Every API endpoint and database query MUST validate user permissions and prevent unauthorized access to resources.

### Agentic Workflow Purity
No manual coding — all implementation via agents/skills using spec → plan → tasks → implement process with Claude Code and Spec-Kit Plus. All development work MUST follow the automated agent workflow without manual intervention.

### Modularity & Reusability
Use sub-agents (Database, Backend, Authentication, Frontend, Integration) and granular skills for every major component. Code components MUST be modular and reusable across the application architecture.

### Production-Ready Code Quality
Type-safe (Pydantic/SQLModel, TypeScript), consistent naming, error handling, proper HTTP status codes. All code MUST be production-ready with appropriate type safety, error handling, and consistent conventions.

### Stateless Authentication
Pure stateless JWT verification on all requests, no shared sessions/DB calls for auth. Authentication system MUST rely solely on JWT tokens without server-side session storage.

## Security Requirements

Authentication: JWT tokens only (Better Auth plugin), shared secret via env (BETTER_AUTH_SECRET), Bearer header on all API calls, 401 Unauthorized on invalid/missing token. API behavior: All endpoints prefixed /api/{user_id}/chat, filter/mutate only by authenticated user_id from decoded JWT, 403 Forbidden on user_id mismatch.

## Development Standards

All endpoints MUST follow the pattern /api/{user_id}/chat with proper user_id validation from JWT. Database: SQLModel models with user_id foreign key, ownership enforced in every query, timestamps (created_at/updated_at), no raw SQL unless necessary. Frontend: Responsive UI (mobile-first), protected routes, automatic JWT attachment in API client, handle 401 → redirect to login.

Code quality: Use Pydantic/SQLModel for models, React Hook Form or native validation in forms, no console.logs in production code, consistent folder structure. Environment: All secrets/config via .env (never hardcoded), NEXT_PUBLIC_API_URL for frontend, load_dotenv in backend.

## Governance

Constitution serves as the authoritative guide for all development decisions. All implementation work MUST comply with these principles. Any deviations require explicit constitutional amendment process.

**Version**: 1.0.0 | **Ratified**: 2026-02-08 | **Last Amended**: 2026-02-08