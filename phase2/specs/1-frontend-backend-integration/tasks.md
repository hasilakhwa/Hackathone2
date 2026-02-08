# Tasks: Frontend-Backend Integration for Todo App

## Phase 0: Environment Verification
- [X] Task 1: Verify `BETTER_AUTH_SECRET` is identical in frontend `.env.local` and backend `.env`.
- [X] Task 2: Check `NEXT_PUBLIC_API_URL` is set to `http://localhost:8000` in frontend `.env.local`.
- [X] Task 3: Ensure both backend and frontend services can be started independently.
- [X] Task 4: Verify the API endpoints exist and are accessible on the backend service.

## Phase 1: Backend Configuration
- [X] Task 5: Add CORS middleware to FastAPI backend (`backend/src/main.py`) to allow requests from `http://localhost:3000`.
- [X] Task 6: Test basic API connectivity between frontend and backend after CORS configuration.
- [ ] Task 7: Verify JWT token validation works correctly on backend endpoints.
- [ ] Task 8: Ensure `user_id` parameter correctly isolates user data on backend.

## Phase 2: Frontend Enhancement
- [X] Task 9: Update API client in `frontend/haisy-todo-app/lib/api.ts` with enhanced error handling for 401, 403, and 404 errors.
- [X] Task 10: Implement toast notifications (using Sonner) for different API error scenarios on the frontend.
- [X] Task 11: Ensure proper JWT token attachment to all authenticated API calls from the frontend.

## Phase 3: Authentication Flow Testing
- [ ] Task 12: Test complete user signup flow from frontend to backend.
- [ ] Task 13: Verify user login flow with token issuance, storage, and session management.
- [ ] Task 14: Confirm redirect to `/tasks` dashboard after successful authentication.
- [ ] Task 15: Test user logout functionality and session clearing on the frontend.

## Phase 4: Task Operations Validation
- [ ] Task 16: Test task creation and association with the correct user account.
- [ ] Task 17: Verify task listing shows only the authenticated user's own tasks.
- [ ] Task 18: Validate task update operations are restricted to task owners.
- [ ] Task 19: Confirm task deletion only works for the user's own tasks.
- [ ] Task 20: Test toggle completion functionality for tasks.

## Phase 5: Security Testing
- [ ] Task 21: Test user isolation: Verify one user cannot access or modify another user's tasks.
- [ ] Task 22: Validate unauthorized access attempts (e.g., no token) return 401 Unauthorized errors.
- [ ] Task 23: Validate unauthorized access attempts (e.g., invalid token) return 401 Unauthorized errors.
- [ ] Task 24: Test that providing a wrong `user_id` in the API path returns a 403 Forbidden error.
- [ ] Task 25: Test that accessing a non-existent or unowned task returns a 404 Not Found error.

## Phase 6: Error Handling & User Experience
- [ ] Task 26: Implement network error handling with user-friendly messages on the frontend.
- [ ] Task 27: Test invalid login attempts and ensure proper error feedback is displayed.
- [ ] Task 28: Test expired token scenarios trigger appropriate redirects to the login page.
- [ ] Task 29: Validate all API calls show appropriate loading and error states on the frontend.

## Phase 7: Documentation & Testing Guide
- [ ] Task 30: Create an integration guide with step-by-step manual test cases.
- [ ] Task 31: Document environment setup and common troubleshooting steps for the integrated application.
- [ ] Task 32: Update `README.md` with instructions on how to run and test both frontend and backend services.