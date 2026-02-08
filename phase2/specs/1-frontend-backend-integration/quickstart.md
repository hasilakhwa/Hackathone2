# Quickstart Guide: Frontend-Backend Integration for Todo App

## Prerequisites
- Node.js 18+ installed for frontend
- Python 3.8+ with uvicorn for backend
- Access to NeonDB database
- Git version control

## Setup Instructions

### 1. Environment Configuration
Ensure the following environment variables are set identically in both frontend and backend:
- In frontend/.env.local: `BETTER_AUTH_SECRET=your-shared-secret`
- In backend/.env: `BETTER_AUTH_SECRET=your-shared-secret`
- In frontend/.env.local: `NEXT_PUBLIC_API_URL=http://localhost:8000`

### 2. Start Backend Service
```bash
cd backend
uvicorn main:app --reload
```
Backend will be available at http://localhost:8000

### 3. Start Frontend Service
```bash
cd frontend/haisy-todo-app
npm run dev
```
Frontend will be available at http://localhost:3000

### 4. Verify Integration
1. Open browser to http://localhost:3000
2. Navigate to signup page and create a new account
3. Verify you can login and access the tasks dashboard
4. Test creating, updating, and deleting tasks
5. Confirm that all API calls are successful in browser dev tools

## Key Features
- User authentication with JWT tokens
- Task management (create, read, update, delete, toggle completion)
- User isolation - each user sees only their own tasks
- Responsive UI with loading states and error handling
- Secure API communication with proper authentication

## Troubleshooting
- If API calls fail, check CORS configuration in backend
- If authentication fails, verify that BETTER_AUTH_SECRET matches in both services
- If tasks aren't appearing, confirm user_id in API paths is correct
- For error handling issues, verify error response format from backend matches frontend expectations