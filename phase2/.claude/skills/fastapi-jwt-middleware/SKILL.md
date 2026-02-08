
```markdown
---
name: fastapi-jwt-middleware
description: Add JWT verification middleware to FastAPI that extracts and validates user from Bearer token. Use for securing all API endpoints.
---

# FastAPI JWT Authentication Middleware

## Instructions

1. **Dependencies**
   - Use python-jose[cryptography] or PyJWT
   - Read BETTER_AUTH_SECRET from env

2. **Middleware logic**
   - Extract Authorization: Bearer <token>
   - Verify signature with shared secret
   - Decode to get user_id, email, exp
   - Attach user to request.state

3. **Error handling**
   - Raise 401 on missing/invalid/expired token

## Best Practices
- Use HS256 algorithm (matches Better Auth default)
- Always validate audience/issuer if set
- Do NOT log full token
- Cache public keys only if using JWKS (not needed here)

## Example Structure

```python
from fastapi import FastAPI, Request, HTTPException, Depends, status
from jose import JWTError, jwt
import os

SECRET = os.getenv("BETTER_AUTH_SECRET")

async def get_current_user(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    token = auth.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        user_id: int = payload.get("sub")  # or "user_id"
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        request.state.user_id = user_id
        request.state.user_email = payload.get("email")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    return user_id

# Usage in router / dependency
@app.get("/api/{user_id}/tasks")
async def list_tasks(user_id: int, current_user: int = Depends(get_current_user)):
    if current_user != user_id:
        raise HTTPException(403, "Forbidden")
    ...