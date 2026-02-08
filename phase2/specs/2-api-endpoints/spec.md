# Feature Specification: RESTful API Backend for Multi-User Todo App

**Feature Branch**: `2-api-endpoints`
**Created**: 2026-02-04
**Status**: Draft
**Input**: User description: "RESTful API backend for multi-user Todo app using FastAPI

Target: Secure, user-isolated task management API that integrates with PostgreSQL DB

Focus: Implement all required CRUD + complete toggle endpoints with authentication checks

Success criteria:
- All endpoints under /api/{user_id}/tasks prefix
- GET / → list only authenticated user's tasks
- POST / → create task owned by authenticated user
- GET /{id}, PUT /{id}, DELETE /{id}, PATCH /{id}/complete → only if task belongs to user
- JWT verification middleware: extract Bearer token, decode, attach user_id to request
- Return 401 Unauthorized if no/invalid token
- Return 403 Forbidden if user_id in path mismatches authenticated user
- Return 404 if task not found or not owned
- Use Pydantic/SQLModel for request/response models

Constraints:
- Use FastAPI + SQLModel only
- Depend on existing database/models from previous spec (get_session, Task model)
- JWT verification using python-jose or PyJWT with BETTER_AUTH_SECRET from env
- No frontend code o"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Secure Task Listing (Priority: P1)

As a user of the Todo application, I want to securely list my tasks so that I can see only my own tasks and not others' tasks.

**Why this priority**: This is fundamental to the basic functionality of a todo app - users need to see their tasks, and security is paramount.

**Independent Test**: A user with valid JWT token can list their tasks and only sees tasks they own, while requests with invalid tokens return 401 Unauthorized.

**Acceptance Scenarios**:

1. **Given** an authenticated user with valid JWT and existing tasks, **When** they call GET /api/{user_id}/tasks with their user_id, **Then** they receive a 200 OK response with only their tasks
2. **Given** a user with no JWT token, **When** they call GET /api/{user_id}/tasks, **Then** they receive a 401 Unauthorized response
3. **Given** a user with invalid/expired JWT token, **When** they call GET /api/{user_id}/tasks, **Then** they receive a 401 Unauthorized response

---

### User Story 2 - Secure Task Creation (Priority: P1)

As a user of the Todo application, I want to securely create new tasks so that my tasks are properly attributed to me and isolated from other users.

**Why this priority**: Creating tasks is fundamental to the todo app functionality, and proper security ensures user data isolation.

**Independent Test**: A user with valid JWT can create a task and it's properly associated with their account, while attempts without authentication fail.

**Acceptance Scenarios**:

1. **Given** an authenticated user with valid JWT, **When** they call POST /api/{user_id}/tasks with task data and their user_id, **Then** they receive a 201 Created response with the created task
2. **Given** an authenticated user with valid JWT, **When** they call POST /api/{user_id}/tasks with another user's user_id, **Then** they receive a 403 Forbidden response
3. **Given** a user without authentication, **When** they call POST /api/{user_id}/tasks, **Then** they receive a 401 Unauthorized response

---

### User Story 3 - Secure Task Operations (Priority: P2)

As a user of the Todo application, I want to securely view, update, delete, and toggle completion status of my tasks so that I can manage them while maintaining data isolation.

**Why this priority**: Complete CRUD operations are needed for full task management functionality with security guarantees.

**Independent Test**: Users can only perform operations on tasks they own, and receive appropriate responses for unauthorized attempts.

**Acceptance Scenarios**:

1. **Given** an authenticated user with valid JWT and owning a specific task, **When** they call GET /api/{user_id}/tasks/{task_id} with correct user_id and task_id, **Then** they receive a 200 OK response with the task
2. **Given** an authenticated user trying to access another user's task, **When** they call GET /api/{user_id}/tasks/{task_id}, **Then** they receive a 404 Not Found response
3. **Given** an authenticated user updating their own task, **When** they call PUT /api/{user_id}/tasks/{task_id}, **Then** they receive a 200 OK response with updated task
4. **Given** a user attempting to update another user's task, **When** they call PUT /api/{user_id}/tasks/{task_id}, **Then** they receive a 404 Not Found response
5. **Given** an authenticated user toggling completion of their own task, **When** they call PATCH /api/{user_id}/tasks/{task_id}/complete, **Then** they receive a 200 OK response with the updated task
6. **Given** an authenticated user attempting to delete their own task, **When** they call DELETE /api/{user_id}/tasks/{task_id}, **Then** they receive a 204 No Content response

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a GET /api/{user_id}/tasks endpoint that returns only tasks belonging to the authenticated user
- **FR-002**: System MUST provide a POST /api/{user_id}/tasks endpoint that creates tasks assigned to the authenticated user
- **FR-003**: System MUST provide a GET /api/{user_id}/tasks/{id} endpoint that returns a specific task only if it belongs to the authenticated user
- **FR-004**: System MUST provide a PUT /api/{user_id}/tasks/{id} endpoint that updates a task only if it belongs to the authenticated user
- **FR-005**: System MUST provide a DELETE /api/{user_id}/tasks/{id} endpoint that deletes a task only if it belongs to the authenticated user
- **FR-006**: System MUST provide a PATCH /api/{user_id}/tasks/{id}/complete endpoint that toggles the completion status of a task only if it belongs to the authenticated user
- **FR-007**: System MUST validate JWT tokens in all endpoints using BETTER_AUTH_SECRET from environment
- **FR-008**: System MUST extract user_id from the authenticated JWT token and compare it with the user_id in the URL path
- **FR-009**: System MUST return 401 Unauthorized for requests with no/invalid JWT tokens
- **FR-010**: System MUST return 403 Forbidden when user_id in path mismatches the authenticated user_id
- **FR-011**: System MUST return 404 Not Found when attempting to access a task that doesn't belong to the authenticated user
- **FR-012**: System MUST use Pydantic models for request and response validation
- **FR-013**: System MUST integrate with existing database/models from previous specification
- **FR-014**: System MUST validate task data according to the existing Task model constraints

### Key Entities *(include if feature involves data)*

- **Authenticated User**: Represents the currently authenticated user identified by JWT token, with user_id that must match the user_id in the URL path for authorized operations
- **Task Operations**: Represent CRUD operations on tasks with security checks ensuring the authenticated user can only operate on tasks they own

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All API endpoints properly validate JWT tokens and return 401 Unauthorized for invalid tokens 100% of the time
- **SC-002**: All endpoints correctly check user_id matching and return 403 Forbidden for mismatches 100% of the time
- **SC-003**: All endpoints correctly enforce task ownership and return 404 for unauthorized access attempts 100% of the time
- **SC-004**: All endpoints perform CRUD operations successfully for authorized requests with response times under 500ms
- **SC-005**: API endpoints properly validate request data using Pydantic models and return 422 for invalid data