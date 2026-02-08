# Implementation Plan: JWT Authentication Bridge with Better Auth and FastAPI

**Branch**: `3-auth-jwt` | **Date**: 2026-02-04 | **Spec**: [specs/3-auth-jwt/spec.md](specs/3-auth-jwt/spec.md)
**Input**: Feature specification from `/specs/3-auth-jwt/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of JWT-based authentication bridge connecting Next.js frontend with FastAPI backend using Better Auth. This involves configuring Better Auth with JWT plugin on the frontend, setting up backend JWT verification using python-jose, and establishing secure communication between frontend and backend through shared BETTER_AUTH_SECRET.

## Technical Context

**Language/Version**: JavaScript/TypeScript (Node.js 18+), Python 3.9+
**Primary Dependencies**: Better Auth with JWT plugin, python-jose, FastAPI, Next.js App Router
**Storage**: N/A (authentication system, relies on existing database from previous spec)
**Testing**: pytest for backend authentication tests, Jest/Cypress for frontend auth flow tests
**Target Platform**: Web application (Next.js frontend + FastAPI backend)
**Project Type**: Web application
**Performance Goals**: JWT verification under 50ms, authentication flows complete within 5 seconds
**Constraints**: <100ms JWT validation time, strict token expiration enforcement, stateless authentication
**Scale/Scope**: 10,000+ concurrent users with secure authentication, proper token lifecycle management

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Technology Stack Adherence: Uses Better Auth and JWT as required by constitution
- Security-First Design: Implements stateless JWT authentication with proper validation
- Production-Ready Code Quality: Uses type-safe implementations (TypeScript/Pydantic) for auth components
- Stateless Authentication: Pure stateless JWT verification on all requests as mandated
- All authentication follows constitution requirement of JWT tokens with BETTER_AUTH_SECRET

## Project Structure

### Documentation (this feature)

```text
specs/3-auth-jwt/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
frontend/
├── lib/
│   └── auth.ts
└── app/
    └── api/
        └── auth/
            └── [...all]/
                └── route.ts
backend/
└── src/
    └── dependencies/
        └── auth.py
```

**Structure Decision**: Selected Web application structure with separate frontend and backend directories. Frontend contains Better Auth configuration and client-side helpers in lib/auth.ts. Backend contains JWT verification logic extending the existing auth dependency from previous specification. This maintains separation of concerns between frontend and backend authentication concerns.

## Phase 1 Design Details

### Frontend Structure
- `lib/auth.ts`: Contains Better Auth server and client configurations with JWT plugin
- `[...all]/route.ts`: Next.js App Router auth routes for login/signup endpoints

### Backend Structure
- `dependencies/auth.py`: Extends existing get_current_user dependency with JWT validation
- Updates to existing auth dependency to work with Better Auth issued JWTs

### Implementation Steps
1. Configure Better Auth with jwt() plugin and BETTER_AUTH_SECRET
2. Set up Next.js auth routes using [all]/route.ts pattern
3. Create client-side auth helpers with jwtClient functionality
4. Update backend get_current_user to decode Better Auth JWTs and extract user_id
5. Implement proper 401 handling for invalid JWT tokens
6. Test auth flow integration between frontend and backend
