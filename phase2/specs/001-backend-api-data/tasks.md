---
description: "Task list for Backend API & Data Layer implementation"
---

# Tasks: Backend API & Data Layer for Todo Web Application

**Input**: Design documents from `/specs/001-backend-api-data/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `backend/tests/`
- Paths shown below follow the web app structure from plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend project structure per implementation plan
- [x] T002 Initialize Python project with FastAPI, SQLModel, and asyncpg dependencies in backend/requirements.txt
- [x] T003 [P] Configure linting and formatting tools (black, flake8, mypy) in backend/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Setup database schema and migrations framework in backend/src/core/database.py
- [x] T005 [P] Implement JWT authentication framework in backend/src/core/security.py
- [x] T006 [P] Setup API routing and middleware structure in backend/src/main.py
- [x] T007 Create base models/entities that all stories depend on in backend/src/models/base.py
- [x] T008 Configure error handling and logging infrastructure in backend/src/core/config.py
- [x] T009 Setup environment configuration management in backend/src/core/config.py
- [x] T010 Create database connection utilities in backend/src/core/database.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Access Personal Tasks via API (Priority: P1) 🎯 MVP

**Goal**: Allow authenticated users to access their personal tasks through the backend API with proper JWT authentication and user isolation

**Independent Test**: Can authenticate with a valid JWT and perform CRUD operations on tasks, delivering the fundamental task management capability.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Contract test for GET /api/{user_id}/tasks endpoint in backend/tests/contract/test_tasks_contract.py
- [ ] T012 [P] [US1] Contract test for POST /api/{user_id}/tasks endpoint in backend/tests/contract/test_tasks_contract.py
- [ ] T013 [P] [US1] Integration test for task access with valid JWT in backend/tests/integration/test_task_access.py

### Implementation for User Story 1

- [x] T014 [P] [US1] Create Task model in backend/src/models/task.py
- [x] T015 [P] [US1] Create User model in backend/src/models/user.py
- [x] T016 [US1] Implement TaskService in backend/src/services/task_service.py (depends on T014, T015)
- [x] T017 [US1] Implement JWT dependency handler in backend/src/api/deps.py
- [x] T018 [US1] Implement GET /api/{user_id}/tasks endpoint in backend/src/api/v1/tasks.py
- [x] T019 [US1] Implement POST /api/{user_id}/tasks endpoint in backend/src/api/v1/tasks.py
- [x] T020 [US1] Add validation and error handling for task operations
- [x] T021 [US1] Add logging for task operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Secure Task Operations (Priority: P1)

**Goal**: Verify JWT tokens for all requests and enforce user identity from JWT payload rather than trusting user_id from request parameters

**Independent Test**: Can be fully tested by attempting various API operations with valid and invalid tokens, delivering the security guarantee.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T022 [P] [US2] Contract test for unauthorized access to endpoints in backend/tests/contract/test_auth_contract.py
- [ ] T023 [P] [US2] Contract test for invalid JWT handling in backend/tests/contract/test_auth_contract.py
- [ ] T024 [P] [US2] Integration test for cross-user access prevention in backend/tests/integration/test_security.py

### Implementation for User Story 2

- [x] T025 [P] [US2] Enhance JWT validation dependency to extract user_id from token in backend/src/api/deps.py
- [x] T026 [US2] Implement user_id validation to ensure URL parameter matches JWT user_id in backend/src/api/deps.py
- [x] T027 [US2] Add 401 Unauthorized response handling in backend/src/api/v1/tasks.py
- [x] T028 [US2] Add 403 Forbidden response for cross-user access attempts in backend/src/api/v1/tasks.py
- [x] T029 [US2] Update all existing endpoints to enforce JWT validation
- [x] T030 [US2] Add comprehensive error responses for authentication failures

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Persistent Task Storage (Priority: P2)

**Goal**: Store and retrieve task data persistently in Neon Serverless PostgreSQL database using SQLModel

**Independent Test**: Can be fully tested by creating tasks, verifying they're stored, and retrieving them later, delivering data durability.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T031 [P] [US3] Integration test for task persistence in backend/tests/integration/test_persistence.py
- [ ] T032 [P] [US3] Unit test for TaskService database operations in backend/tests/unit/test_task_service.py

### Implementation for User Story 3

- [x] T033 [P] [US3] Enhance Task model with proper SQLModel relationships in backend/src/models/task.py
- [x] T034 [P] [US3] Enhance User model with proper SQLModel relationships in backend/src/models/user.py
- [x] T035 [US3] Implement database session management in backend/src/services/task_service.py
- [x] T036 [US3] Add database transaction handling for task operations in backend/src/services/task_service.py
- [x] T037 [US3] Add indexes and constraints per data model requirements in backend/src/models/task.py
- [x] T038 [US3] Add database connection pooling configuration in backend/src/core/database.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Task CRUD Operations (Priority: P2)

**Goal**: Implement complete CRUD functionality for tasks including GET, PUT, PATCH, DELETE operations

**Independent Test**: Can be fully tested by performing all CRUD operations on tasks, delivering complete task management capability.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T039 [P] [US4] Contract test for GET /api/{user_id}/tasks/{id} endpoint in backend/tests/contract/test_crud_contract.py
- [ ] T040 [P] [US4] Contract test for PUT /api/{user_id}/tasks/{id} endpoint in backend/tests/contract/test_crud_contract.py
- [ ] T041 [P] [US4] Contract test for DELETE /api/{user_id}/tasks/{id} endpoint in backend/tests/contract/test_crud_contract.py
- [ ] T042 [P] [US4] Contract test for PATCH /api/{user_id}/tasks/{id}/complete endpoint in backend/tests/contract/test_crud_contract.py

### Implementation for User Story 4

- [x] T043 [P] [US4] Implement GET /api/{user_id}/tasks/{id} endpoint in backend/src/api/v1/tasks.py
- [x] T044 [P] [US4] Implement PUT /api/{user_id}/tasks/{id} endpoint in backend/src/api/v1/tasks.py
- [x] T045 [P] [US4] Implement DELETE /api/{user_id}/tasks/{id} endpoint in backend/src/api/v1/tasks.py
- [x] T046 [US4] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint in backend/src/api/v1/tasks.py
- [ ] T047 [US4] Add request/response validation models for CRUD operations in backend/src/api/v1/tasks.py
- [ ] T048 [US4] Add comprehensive error handling for all CRUD operations
- [ ] T049 [US4] Add consistent JSON response structures for all endpoints

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T050 [P] Documentation updates in backend/docs/
- [ ] T051 Code cleanup and refactoring
- [ ] T052 Performance optimization across all stories
- [ ] T053 [P] Additional unit tests (if requested) in backend/tests/unit/
- [ ] T054 Security hardening
- [ ] T055 Run quickstart.md validation
- [ ] T056 Add comprehensive API documentation in backend/src/main.py
- [ ] T057 Add health check endpoint in backend/src/api/v1/

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for GET /api/{user_id}/tasks endpoint in backend/tests/contract/test_tasks_contract.py"
Task: "Contract test for POST /api/{user_id}/tasks endpoint in backend/tests/contract/test_tasks_contract.py"
Task: "Integration test for task access with valid JWT in backend/tests/integration/test_task_access.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in backend/src/models/task.py"
Task: "Create User model in backend/src/models/user.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence