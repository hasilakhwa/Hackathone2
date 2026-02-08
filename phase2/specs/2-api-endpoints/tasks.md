---
description: "Task list for JWT Authentication Bridge with Better Auth and FastAPI implementation"
---

# Tasks: JWT Authentication Bridge with Better Auth and FastAPI

**Input**: Design documents from `/specs/2-api-endpoints/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume web app structure based on plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Install Better Auth dependencies in frontend directory
- [X] T002 [P] Install python-jose or PyJWT in backend/requirements.txt
- [X] T003 Configure shared BETTER_AUTH_SECRET in both frontend and backend .env files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create frontend/lib/auth.ts with Better Auth server configuration and JWT plugin
- [X] T005 Create frontend/app/api/auth/[...all]/route.ts with Next.js auth routes
- [X] T006 Update backend/src/dependencies/auth.py to extend get_current_user with JWT verification
- [X] T007 Create client-side auth helpers using better-auth/client with jwtClient plugin
- [X] T008 Implement JWT token validation logic in backend using python-jose and BETTER_AUTH_SECRET from env

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure User Registration (Priority: P1) 🎯 MVP

**Goal**: Enable new users to securely register an account and receive JWT token for API access

**Independent Test**: A new user can sign up with their email and receive a JWT token, which can then be used to access protected API endpoints.

### Implementation for User Story 1

- [X] T009 [US1] Create signup page component in frontend/app/signup/page.tsx
- [X] T010 [US1] Implement signup form with Better Auth client integration in signup page
- [X] T011 [US1] Test that successful signup returns JWT token in frontend
- [X] T012 [US1] Verify JWT token from signup can be used for protected API calls in backend

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Secure User Login (Priority: P1)

**Goal**: Enable existing users to securely log in to their account and receive JWT token for API access

**Independent Test**: An existing user can log in with their credentials and receive a JWT token that authenticates subsequent API requests.

### Implementation for User Story 2

- [X] T013 [US2] Create login page component in frontend/app/login/page.tsx
- [X] T014 [US2] Implement login form with Better Auth client integration in login page
- [X] T015 [US2] Test that successful login returns JWT token in frontend
- [X] T016 [US2] Verify JWT token from login can be used for protected API calls in backend

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Secure API Access (Priority: P2)

**Goal**: Enable registered users with valid JWT tokens to access protected API endpoints securely

**Independent Test**: A user with a valid JWT token can access protected API endpoints, while requests without tokens or with invalid tokens are rejected with appropriate error responses.

### Implementation for User Story 3

- [X] T017 [US3] Create apiFetch utility in frontend/lib/api.ts that attaches Bearer token to requests
- [X] T018 [US3] Update existing task endpoints to validate JWT tokens from Authorization header
- [X] T019 [US3] Ensure user_id from JWT matches user_id in API endpoint path for all protected endpoints
- [X] T020 [US3] Return proper 401 Unauthorized responses for invalid/missing JWT tokens
- [X] T021 [US3] Return proper 403 Forbidden responses for user_id mismatch in path vs token

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T022 [P] Update documentation with authentication setup instructions in specs/2-api-endpoints/quickstart.md
- [X] T023 Add proper error handling for authentication failures in both frontend and backend
- [X] T024 [P] Create API usage examples with authentication in docs/
- [X] T025 Update environment configuration documentation in README.md
- [X] T026 Run authentication flow integration tests to verify complete functionality

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 → P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May reuse auth configuration from US1
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Depends on JWT availability from US1/US2

### Within Each User Story

- Frontend authentication components before API usage
- JWT token retrieval before attaching to API requests
- Core functionality before error handling and validation

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- User Story 1 and 2 can be developed in parallel after foundational phase
- Different user stories can be worked on sequentially by priority