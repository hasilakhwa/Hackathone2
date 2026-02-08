---
id: 1
title: "update-project-constitution"
stage: constitution
date_iso: "2026-02-04"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "001-todo-app"
user: "Claude Sonnet 4.5"
command: "/sp.constitution"
labels: ["constitution", "security", "standards"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
 - ".specify/memory/constitution.md"
tests_yaml:
 - "none"
---

# CONSTITUTION UPDATE TASK

## Original Prompt
```
Project: Multi-user Todo Full-Stack Web Application (Basic Level)

Core principles:
- Strict adherence to provided technology stack: Next.js 16+ (App Router), FastAPI (Python), SQLModel ORM, Neon Serverless PostgreSQL, Better Auth with JWT
- Security-first: Enforce user isolation, stateless JWT auth, no cross-user data access, always verify ownership
- Agentic workflow purity: No manual coding — all implementation via agents/skills using spec → plan → tasks → implement process
- Modularity & reusability: Use sub-agents (Database, Backend, Authentication, Frontend, Integration) and granular skills for every major component
- Clean, production-ready code: Type-safe (Pydantic/SQLModel, TypeScript), consistent naming, error handling, proper HTTP status codes

Key standards:
- Authentication: JWT tokens only (Better Auth plugin), shared secret via env (BETTER_AUTH_SECRET), Bearer header on all API calls, 401 Unauthorized on invalid/missing token
- API behavior: All endpoints prefixed /api/{user_id}/tasks, filter/mutate only by authenticated user_id from decoded JWT, 403 Forbidden on user_id mismatch
- Database: SQLModel models with user_id foreign key, ownership enforced in every query, timestamps (created_at/updated_at), no raw SQL unless necessary
- Frontend: Responsive UI (mobile-first), protected routes, automatic JWT attachment in API client, handle 401 → redirect to login
- Code quality: Use Pydantic/SQLModel for models, React Hook Form or native validation in forms, no console.logs in production code, consistent folder structure
- Environment: All secrets/config via .env (never hardcoded), NEXT_PUBLIC_API_URL for frontend, load_dotenv in backend
- Testing mindset: Agents should include basic validation (e.g., ownership checks, error responses), plan for future unit/integration tests

Constraints:
- Feature scope: Only 5 basic CRUD + complete toggle for tasks (no extras like due dates, categories, search unless later specified)
- No shared sessions/DB calls for auth: Pure stateless JWT verification on
```

## Response Summary
Updated the project constitution file (.specify/memory/constitution.md) to reflect the multi-user Todo application requirements, incorporating all specified principles around technology stack adherence, security-first design, agentic workflow purity, modularity, and production-ready code quality.

## Outcome Impact
Successfully created a comprehensive constitution document that defines the core principles and standards for the multi-user Todo application project. The document now properly guides development with clear technology stack requirements, security standards, and workflow procedures.

## Files Summary
- .specify/memory/constitution.md: Updated with new constitution content reflecting multi-user Todo application requirements

## Tests Summary
No tests were involved in this constitution update task.

## Next Prompts
Consider running /sp.specify to create a feature specification based on this constitution, or /sp.plan to develop an implementation plan.

## Reflection Note
Creating a well-defined constitution upfront helps ensure consistent development practices across the team and project lifecycle.

## Failure Modes Observed
None observed in this prompt execution.

## Next Experiment to Improve Prompt Quality
N/A

## Acceptance Criteria Check
- [X] Core principles properly documented
- [X] Technology stack requirements clearly defined
- [X] Security standards properly outlined
- [X] Workflow procedures established
- [X] File properly saved to correct location