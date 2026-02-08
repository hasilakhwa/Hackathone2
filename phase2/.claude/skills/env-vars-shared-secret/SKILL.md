
```markdown
---
name: env-vars-shared-secret
description: Manage shared environment variables like BETTER_AUTH_SECRET and NEON_DATABASE_URL across frontend/backend. Use for secure config setup.
---

# Shared Environment Variables Setup

## Instructions

1. **.env file**
   - BETTER_AUTH_SECRET=super-long-secret
   - NEON_DATABASE_URL=postgres://...
   - NEXT_PUBLIC_API_URL=http://localhost:8000

2. **Frontend**
   - NEXT_PUBLIC_ for client-exposed vars

3. **Backend**
   - Load with os.getenv or pydantic-settings

4. **Security**
   - Never commit .env

## Best Practices
- Use .env.example template
- Different secrets per env (dev/prod)
- Rotate secrets periodically
- Use secrets manager in production

## Example Structure

```bash
# .env.example
BETTER_AUTH_SECRET=
NEON_DATABASE_URL=
NEXT_PUBLIC_API_URL=

# backend .env
# same as above

# In FastAPI startup:
from dotenv import load_dotenv
load_dotenv()