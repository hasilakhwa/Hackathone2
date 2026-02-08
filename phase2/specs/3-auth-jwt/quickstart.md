# Quickstart: JWT Authentication Bridge with Better Auth and FastAPI

## Prerequisites

- Node.js 18+ for Better Auth
- Python 3.9+ for FastAPI backend
- Better Auth library installed in frontend
- python-jose or PyJWT installed in backend
- BETTER_AUTH_SECRET configured in .env files

## Installation

### 1. Frontend: Better Auth Setup

```bash
# Install Better Auth with JWT plugin
npm install @better-auth/node @better-auth/node/plugins
# or
yarn add @better-auth/node @better-auth/node/plugins
```

### 2. Backend: JWT Verification Dependencies

```bash
# Install python-jose for JWT verification
pip install python-jose[cryptography]
# or using poetry
poetry add python-jose[cryptography]
```

### 3. Environment Configuration

Create/update your `.env` files to include the shared secret:

Frontend (.env.local):
```env
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
BETTER_AUTH_SECRET=your-super-secret-key-here
```

Backend (backend/.env):
```env
BETTER_AUTH_SECRET=your-super-secret-key-here
NEON_DATABASE_URL=postgresql://...
```

## Frontend Implementation

### 1. Configure Better Auth with JWT Plugin

```typescript
// lib/auth.ts
import { betterAuth } from "@better-auth/node";
import { jwt } from "@better-auth/node/plugins";

export const auth = betterAuth({
  secret: process.env.BETTER_AUTH_SECRET!,
  plugins: [
    jwt({
      secret: process.env.BETTER_AUTH_SECRET!,
      expiresIn: "7d", // Token expires in 7 days
    }),
  ],
  // other auth configuration...
});
```

### 2. Create Auth Routes

```typescript
// app/api/auth/[...all]/route.ts
import { auth } from "@/lib/auth";

export const { GET, POST } = auth;
```

### 3. Client-Side API Calls with Token

```typescript
// lib/api.ts
import { getAccessToken } from "@better-auth/client/plugins";

const apiFetch = async (url: string, options: RequestInit = {}) => {
  const token = await getAccessToken();

  const headers = {
    ...options.headers,
    Authorization: token ? `Bearer ${token.jwt}` : "",
  };

  return fetch(url, {
    ...options,
    headers,
  });
};
```

## Backend Implementation

### 1. Update get_current_user Dependency

```python
# backend/src/dependencies/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

security = HTTPBearer()
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET")
ALGORITHM = "HS256"

class TokenData(BaseModel):
    user_id: int
    email: str

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    """
    Extract and validate user data from JWT token.
    """
    token = credentials.credentials

    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        email: str = payload.get("email")

        if user_id is None or email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token_data = TokenData(user_id=user_id, email=email)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token_data
```

### 2. Apply Authentication to API Routes

```python
# backend/src/routers/tasks.py (example)
from fastapi import APIRouter, Depends
from .dependencies.auth import get_current_user

router = APIRouter()

@router.get("/api/{user_id}/tasks")
def get_user_tasks(
    user_id: int,
    current_user: TokenData = Depends(get_current_user)
):
    # Verify user_id in path matches authenticated user_id
    if current_user.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: Cannot access another user's tasks"
        )

    # Return user's tasks...
    return {"tasks": []}
```

## Usage

### 1. User Registration/Login Flow

```typescript
// Example signup/login flow
import { signIn, signUp } from "@better-auth/client";

// Sign up new user
const newUser = await signUp("email", {
  email: "user@example.com",
  password: "securePassword",
});

// Sign in existing user
const session = await signIn("email", {
  email: "user@example.com",
  password: "securePassword",
});
```

### 2. Making Authenticated API Calls

```typescript
// Use the apiFetch helper to make authenticated calls
const response = await apiFetch('/api/1/tasks', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
  },
});
```

## Development Commands

### Run Both Frontend and Backend

Frontend:
```bash
npm run dev
```

Backend:
```bash
cd backend
uvicorn src.main:app --reload
```

### Test Authentication

```bash
# Test registration
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password123"}'

# Test protected endpoint with JWT
curl -X GET http://localhost:8000/api/1/tasks \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```

## Security Notes

- Always validate that the user_id from JWT matches the user_id in the request path
- Use HTTPS in production to protect JWT tokens in transit
- Implement proper token expiration and refresh mechanisms
- Never log JWT tokens or their contents
- Ensure BETTER_AUTH_SECRET is strong and kept secure