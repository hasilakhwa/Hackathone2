---
description: "Task list for SQLModel-based multi-user todo database schema implementation"
---

# Tasks: Persistent Multi-User Task Storage

**Input**: Design documents from `/specs/1-db-schema/`
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

- [X] T001 Create backend directory structure
- [X] T002 [P] Initialize Python project with SQLModel, SQLAlchemy, python-dotenv dependencies in backend/
- [X] T003 [P] Configure .env file with NEON_DATABASE_URL placeholder

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create backend/src/core/database.py for SQLModel database configuration
- [X] T005 [P] Create backend/src/models/__init__.py for User and Task models
- [X] T006 Configure environment loading and database connection in database.py
- [X] T007 Implement session dependency function for FastAPI in database.py
- [X] T008 Add database initialization function using SQLModel.metadata.create_all()

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - User Data Isolation (Priority: P1) 🎯 MVP

**Goal**: Enable proper user isolation so each user can only access their own tasks

**Independent Test**: System can store and retrieve tasks for multiple users independently without cross-contamination

### Implementation for User Story 1

- [X] T009 [P] [US1] Define User model with id, email, timestamps in backend/src/models/__init__.py
- [X] T010 [P] [US1] Define Task model with title, description, completed, timestamps, user_id in backend/src/models/__init__.py
- [X] T011 [US1] Add relationship between User and Task models in backend/src/models/__init__.py
- [X] T012 [US1] Implement foreign key constraint from Task.user_id to User.id in models
- [X] T013 [US1] Add unique constraint to User.email field in User model
- [X] T014 [US1] Create test to verify user isolation (one user can't access another's tasks) in backend/tests/unit/test_models.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Basic Task Persistence (Priority: P1)

**Goal**: Ensure tasks persist across application restarts and can be retrieved reliably

**Independent Test**: A task created by a user can be retrieved after the application restarts

### Implementation for User Story 2

- [X] T015 [US2] Create database connection test in backend/tests/integration/test_database_connection.py
- [X] T016 [US2] Implement task CRUD operations in backend/src/core/database.py
- [X] T017 [US2] Add functionality to create tasks linked to users in database.py
- [X] T018 [US2] Add functionality to retrieve tasks by user_id in database.py
- [X] T019 [US2] Create test to verify task persistence across restarts in backend/tests/integration/test_persistence.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Task Data Integrity (Priority: P2)

**Goal**: Ensure database enforces data integrity to prevent inconsistent or corrupted data

**Independent Test**: Database prevents invalid data states from being stored (like orphaned tasks without users)

### Implementation for User Story 3

- [X] T020 [US3] Add validation to prevent creating tasks without valid user_id in database.py
- [X] T021 [US3] Implement proper error handling for invalid foreign key references
- [X] T022 [US3] Add database indexes for improved query performance on user_id in models
- [X] T023 [US3] Create test to verify foreign key constraints prevent orphaned tasks in backend/tests/unit/test_integrity.py
- [X] T024 [US3] Add input validation for Task model fields in models/__init__.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T025 [P] Update documentation with database setup instructions in specs/1-db-schema/quickstart.md
- [X] T026 Add proper error logging for database operations in backend/src/core/database.py
- [X] T027 [P] Create sample usage examples in backend/examples/database_usage.py
- [X] T028 Run all tests to verify complete functionality
- [X] T029 Update environment configuration documentation in README.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 → P1 → P2)
- **Polish (Final Phase)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 models
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 models and US2 implementation

### Within Each User Story

- Models before services
- Services before validation
- Core implementation before integration

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Models within User Story 1 marked [P] can run in parallel
- Different user stories can be worked on sequentially by priority

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Define User model with id, email, timestamps in backend/src/models/__init__.py"
Task: "Define Task model with title, description, completed, timestamps, user_id in backend/src/models/__init__.py"
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
5. Each story adds value without breaking previous stories

---

## Notes

- [P] tasks = different files, no dependencies
- [US1], [US2], [US3] labels map tasks to specific user stories for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Verify all dependencies are met before starting a task