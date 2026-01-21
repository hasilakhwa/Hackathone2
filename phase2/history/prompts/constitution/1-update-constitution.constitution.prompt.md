---
id: 1
title: "Update Constitution for Todo App"
stage: constitution
date_iso: "2026-01-20"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "todo-fullstack-web-app"
branch: "001-todo-app"
user: "user"
command: "/sp.constitution"
labels: ["constitution", "todo-app", "hackathon"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
  - "history/prompts/constitution/1-update-constitution.constitution.prompt.md"
tests_yaml: []
---

# Update Constitution for Todo App

## User Input
```
/sp.constitution

Project: Todo Full-Stack Web Application (Agentic Dev Stack – Hackathon Phase 2)

Core principles:
- Agentic-first development (spec → plan → tasks → implementation)
- No manual coding (all code generated via Claude Code)
- Clear separation of concerns across specs (Backend, Auth, Frontend)
- Security-by-design (auth enforced at every layer)
- Production-grade structure despite hackathon scope

Key standards:
- Every feature must be traceable to an explicit requirement
- Every API endpoint must map to a documented behavior
- Authentication must be enforced on all protected routes
- User data isolation must be guaranteed at the backend layer
- JWT-based auth must be stateless and verifiable independently
- Frontend must never assume trust without backend verification
- All generated code must be runnable without manual edits

Technology constraints:
- Frontend: Next.js 16+ using App Router
- Backend: Python FastAPI
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth (JWT-based)
- Auth secret shared via BETTER_AUTH_SECRET environment variable

Security standards:
- All API endpoints require a valid JWT token after authentication
- Requests without a token must return 401 Unauthorized
- Backend must validate JWT signature and expiration
- User ID must be derived from JWT, not trusted from client input
- Task ownership must be enforced on every CRUD operation
- No cross-user data access under any circumstances

API standards:
- RESTful conventions must be followed
- HTTP methods must match intent (GET, POST, PUT, PATCH, DELETE)
- Consistent JSON response shapes
- Proper HTTP status codes for success and failure cases
- Clear error messages without leaking sensitive data

Frontend standards:
- Responsive UI across desktop and mobile
- Auth-aware routing (protected vs public pages)
- API client must automatically attach JWT token
- Loading, error, and empty states must be handled explicitly
- UI must reflect backend truth (no fake optimistic state)

Agentic workflow rules:
- Each spec must have its own sp.specify prompt
- Each sp.specify must result in a concrete execution plan
- Plans must be broken into deterministic, testable tasks
- No implementation before plan approval
- Iteration is allowed, silent deviation is not

Documentation & evaluation readiness:
- Specs must be readable by judges without extra context
- Plans must clearly show reasoning and ordering
- Decisions must be explicit, not implied
- Tradeoffs must be stated when relevant

Success criteria:
- All 5 Basic Level features implemented as a working web app
- Multi-user task isolation verified end-to-end
- JWT authentication works across frontend and backend
- Backend persists data correctly in Neon PostgreSQL
- Frontend fully functional using generated code only
- Entire workflow demonstrates proper Agentic Dev Stack usage
```

## Response Summary
Updated the project constitution file (.specify/memory/constitution.md) to reflect the Todo Full-Stack Web Application requirements. The new constitution includes:

- Six core principles covering agentic-first development, no manual coding, separation of concerns, security-by-design, production-grade structure, and traceability
- Detailed technology stack requirements for Next.js, FastAPI, SQLModel, Neon PostgreSQL, and Better Auth
- Comprehensive security standards including JWT-based authentication and user data isolation
- API and frontend standards for consistent development
- Agentic workflow rules for spec-driven development
- Success criteria aligned with hackathon objectives

The constitution now serves as the governing document for the Todo Full-Stack Web Application project, ensuring all development activities follow the specified principles and constraints.

## Outcome
The project constitution has been successfully updated to guide the development of the Todo Full-Stack Web Application using the Agentic Dev Stack methodology. All placeholder values were replaced with specific requirements from the user input, and the document is now ready to govern the project's development lifecycle.