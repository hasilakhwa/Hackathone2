# Feature Specification: JWT Authentication System for Multi-User Todo Web App

**Feature Branch**: `3-auth-jwt`
**Created**: 2026-02-04
**Status**: Draft
**Input**: User description: "Authentication system with JWT for multi-user Todo web app

Target: Secure bridge between Next.js frontend (Better Auth) and FastAPI backend via JWT tokens

Focus: Enable signup/signin on frontend, issue JWT, verify on backend, ensure stateless user isolation

Success criteria:
- Better Auth configured in Next.js with JWT plugin enabled
- JWT issued on successful login/signup with user_id/sub and email
- Backend verifies JWT using same BETTER_AUTH_SECRET (HS256 algorithm)
- Frontend attaches Bearer token to every API request
- Backend dependency extracts user_id from token, attaches to request.state
- Invalid/expired/missing token → 401 Unauthorized
- Token expiry handled (default 7 days or configured)
- Shared secret managed via .env (BETTER_AUTH_SECRET consistent across FE/BE)
- Basic login/signup pages/flows work with redirect on success

Constraints:
- Use Better Auth library only (no custom auth from scratch)
- JWT plugin for Better Auth (enable in server config)
- No session cookies for backend – points or business logic (already in backend spec)
- Database user model details (assume email/id from Better Auth)
- Frontend UI pages beyond basic auth forms
- Refresh tokens or advanced session managementAuthentication system with JWT for multi-user Todo web app

Target: Secure bridge between Next.js frontend (Better Auth) and FastAPI backend via JWT tokens

Focus: Enable signup/signin on frontend, issue JWT, verify on backend, ensure stateless user isolation

Success criteria:
- Better Auth configured in Next.js with JWT plugin enabled
- JWT issued on successful login/signup with user_id/sub and email
- Backend verifies JWT using same BETTER_AUTH_SECRET (HS256 algorithm)
- Frontend attaches Bearer token to every API request
- Backend dependency extracts user_id from token, attaches to request.state
- Invalid/expired/missing token → 401 Unauthorized
- Token expiry handled (default 7 days or configured)
- Shared secret managed via .env (BETTER_AUTH_SECRET consistent across FE/BE)
- Basic login/signup pages/"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Secure User Registration (Priority: P1)

As a new user of the Todo application, I want to securely register an account so that I can access the application and create tasks associated with my identity.

**Why this priority**: This is fundamental to user acquisition - without registration, there are no users, and the entire application cannot function.

**Independent Test**: A new user can sign up with their email and receive a JWT token, which can then be used to access protected API endpoints.

**Acceptance Scenarios**:
1. **Given** a user has opened the registration page, **When** they submit valid registration details, **Then** they receive a successful registration response with JWT token
2. **Given** a user attempts to register with invalid email, **When** they submit the form, **Then** they receive an error message and no token is issued
3. **Given** a user has successfully registered, **When** they attempt to access a protected API endpoint with the issued JWT, **Then** they receive a successful response

---

### User Story 2 - Secure User Login (Priority: P1)

As an existing user of the Todo application, I want to securely log in to my account so that I can access my tasks and continue using the application.

**Why this priority**: This is essential for returning users - without login functionality, users cannot access their existing data.

**Independent Test**: An existing user can log in with their credentials and receive a JWT token that authenticates subsequent API requests.

**Acceptance Scenarios**:
1. **Given** a user has opened the login page, **When** they submit valid login credentials, **Then** they receive a successful login response with JWT token
2. **Given** a user attempts to log in with incorrect credentials, **When** they submit the form, **Then** they receive an error message and no token is issued
3. **Given** a user has successfully logged in, **When** they attempt to access a protected API endpoint with the issued JWT, **Then** they receive a successful response

---

### User Story 3 - Secure API Access (Priority: P2)

As a registered user of the Todo application, I want to access protected API endpoints securely so that my requests are properly authenticated and authorized.

**Why this priority**: This is critical for the application's security model - users need to be able to access their data with proper authentication.

**Independent Test**: A user with a valid JWT token can access protected API endpoints, while requests without tokens or with invalid tokens are rejected with appropriate error responses.

**Acceptance Scenarios**:
1. **Given** a user has a valid JWT token, **When** they make an API request with proper Bearer authorization header, **Then** the request is processed successfully with user context attached
2. **Given** a user has an expired or invalid JWT token, **When** they make an API request, **Then** they receive a 401 Unauthorized response
3. **Given** a user makes an API request without any token, **When** the request reaches the backend, **Then** they receive a 401 Unauthorized response

---

### Edge Cases

- What happens when a JWT token is malformed or tampered with?
- How does the system handle token expiration during long-running operations?
- What happens when the shared secret (BETTER_AUTH_SECRET) differs between frontend and backend?
- How does the system handle simultaneous requests with an expiring token?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST configure Better Auth in Next.js with JWT plugin enabled
- **FR-002**: System MUST issue JWT tokens on successful login/signup containing user_id/sub and email claims
- **FR-003**: System MUST verify JWT tokens in backend API endpoints using BETTER_AUTH_SECRET with HS256 algorithm
- **FR-004**: System MUST attach Bearer token to every API request from frontend
- **FR-005**: System MUST extract user_id from JWT token and attach to request context in backend
- **FR-006**: System MUST return 401 Unauthorized for invalid/expired/missing JWT tokens
- **FR-007**: System MUST handle JWT token expiry (default 7 days or configurable)
- **FR-008**: System MUST manage shared secret consistently via .env (BETTER_AUTH_SECRET) across frontend and backend
- **FR-009**: System MUST provide basic login/signup pages with proper redirect on success
- **FR-010**: System MUST ensure stateless authentication (no server-side session storage)
- **FR-011**: System MUST validate JWT signature integrity before processing claims
- **FR-012**: System MUST ensure user isolation at the API level based on JWT claims

### Key Entities *(include if feature involves data)*

- **JWT Token**: Represents a user's authenticated session with encrypted claims containing user identity, validity period, and other authentication data
- **User Identity**: Represents the authenticated user with user_id and email extracted from JWT claims for authorization decisions
- **Authorization Context**: Contains authenticated user information attached to API requests for access control decisions

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: User registration completes successfully within 5 seconds with JWT token issued 100% of the time for valid inputs
- **SC-002**: User login completes successfully within 5 seconds with JWT token issued 100% of the time for valid credentials
- **SC-003**: Protected API endpoints authenticate valid JWT tokens within 100ms and reject invalid tokens with 401 response 100% of the time
- **SC-004**: Token validation fails for tampered/malformed JWTs with 401 response within 100ms 100% of the time
- **SC-005**: Frontend successfully attaches JWT Bearer tokens to 100% of protected API requests