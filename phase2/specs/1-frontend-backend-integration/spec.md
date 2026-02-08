# Feature Specification: Full integration and end-to-end testing for Todo web app (backend + frontend connection)

## Overview
Connect existing FastAPI backend with Neon DB to the fresh Next.js frontend, validating the complete multi-user flow. Ensure seamless API communication, JWT authentication, user isolation, and proper error handling.

## User Scenarios & Testing
- As a new user, I want to register/signup through the frontend to create my account
- As a registered user, I want to login through the frontend and be redirected to my tasks dashboard
- As a logged-in user, I want to create tasks that are associated with my account only
- As a logged-in user, I want to view only my own tasks, not tasks from other users
- As a logged-in user, I want to update and delete only my own tasks
- As a logged-in user, I want to toggle task completion status
- As a user, I want to be redirected to login if my session expires or is invalid
- As a user attempting to access another user's tasks, I want to receive an appropriate error message
- As a user, I want to see friendly error messages when something goes wrong
- As a user, I want the frontend and backend to work together without CORS or network errors

Test cases:
- User can successfully sign up through the frontend and see account created
- User can successfully login and be redirected to /tasks dashboard
- User can create a task and see it appear in their personal task list
- User can only see their own tasks, not tasks from other users
- User can update their own tasks but not other users' tasks
- User can delete their own tasks but not other users' tasks
- User can toggle completion status of their own tasks
- When no authentication token exists, user is redirected to login
- When an invalid authentication token is provided, user is redirected to login
- When attempting to access another user's tasks, user receives appropriate error (403)
- When attempting to access a non-existent task, user receives appropriate error (404)
- All user actions provide appropriate feedback through toast notifications
- Both services (frontend and backend) start locally without errors
- API requests complete successfully with proper JWT authentication

## Functional Requirements
1. **API Communication**
   - [REQ-001] System must successfully call backend API endpoints from the frontend with JWT Bearer token authentication
   - [REQ-002] System must handle API requests for user registration, authentication, and task operations
   - [REQ-003] System must validate JWT tokens on both frontend and backend

2. **User Authentication Flow**
   - [REQ-004] System must allow user signup through frontend form that connects to backend API
   - [REQ-005] System must allow user login through frontend form that connects to backend API
   - [REQ-006] System must redirect user to /tasks dashboard after successful login
   - [REQ-007] System must store and manage JWT tokens securely in frontend

3. **Task Operations**
   - [REQ-008] System must allow users to create tasks through frontend connected to backend API
   - [REQ-009] System must allow users to view only their own tasks
   - [REQ-010] System must allow users to update their own tasks
   - [REQ-011] System must allow users to delete their own tasks
   - [REQ-012] System must allow users to toggle task completion status

4. **User Isolation**
   - [REQ-013] System must ensure strict user isolation - each user sees/modifies only their own tasks
   - [REQ-014] System must prevent unauthorized access to other users' data
   - [REQ-015] System must validate that users can only access resources they own

5. **Security Measures**
   - [REQ-016] System must redirect to login when no authentication token is present
   - [REQ-017] System must redirect to login when an invalid authentication token is presented
   - [REQ-018] System must return 403 Forbidden when wrong user_id is in API path
   - [REQ-019] System must return 404 Not Found when task is not found or not owned by user

6. **Error Handling**
   - [REQ-020] System must display user-friendly error messages through toast notifications
   - [REQ-021] System must handle "Session expired" scenarios gracefully
   - [REQ-022] System must handle "Invalid credentials" scenarios with appropriate feedback
   - [REQ-023] System must properly format and display API error responses to users

7. **Environment Configuration**
   - [REQ-024] System must correctly configure environment variables (BETTER_AUTH_SECRET, NEXT_PUBLIC_API_URL)
   - [REQ-025] System must connect to backend at specified API URL (localhost:8000)

## Non-functional Requirements
- Performance: API requests should complete within 3 seconds on local network
- Reliability: System should maintain user data isolation under normal operating conditions
- Security: JWT tokens must be securely stored and transmitted
- Usability: Error messages should be clear and actionable for users
- Compatibility: Application should work in modern browsers without CORS issues
- Maintainability: Frontend and backend should remain decoupled but properly integrated

## Key Entities
- **User**: Authentication entity with credentials, managed by the backend service
- **Task**: Task entity with properties (title, description, completed status, timestamps) tied to specific user
- **Authentication Token**: JWT token that enables API access and verifies user identity
- **Session**: Client-side session state that maintains user authentication status

## Assumptions
- Backend FastAPI service is running at http://localhost:8000
- Backend provides standard CRUD operations for tasks with user_id parameter
- Authentication is handled through JWT tokens with proper expiration
- Database (NeonDB) is properly configured and accessible from the backend
- Both frontend and backend are running simultaneously during integration
- Network connectivity exists between frontend and backend during local development

## Success Criteria
- Users can complete the full flow: Signup → Login → Redirect to /tasks dashboard with zero errors
- All task operations (create, read, update, delete, toggle completion) work correctly through API
- Two different users can each see and modify only their own tasks without data leakage
- Invalid authentication attempts result in appropriate 401 responses and login redirects
- Incorrect user_id in API path results in 403 Forbidden responses
- Non-existent or unauthorized tasks result in 404 responses
- User-friendly error messages appear as toast notifications for all error scenarios
- Both frontend and backend services start without configuration errors
- No CORS or network errors occur during API communication
- End-to-end testing confirms all functional requirements are met