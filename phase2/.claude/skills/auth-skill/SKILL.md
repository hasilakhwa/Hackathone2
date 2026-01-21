---
name: auth-skill
description: Implement secure authentication systems including signup, sign in, password hashing, JWT-based sessions, and Better Auth integration.
---

# Authentication Skill

## Scope

This skill focuses on building **secure, production-ready authentication flows** for modern web applications.  
Use this skill whenever implementing user identity, session management, or access control.

---

## Core Capabilities

1. **User Signup**
   - Validate input (email, password, username)
   - Enforce strong password rules
   - Prevent duplicate accounts
   - Store users securely in the database

2. **User Sign In**
   - Verify credentials securely
   - Handle incorrect login attempts
   - Support email/password authentication
   - Prepare hooks for OAuth or magic links (if needed)

3. **Password Security**
   - Hash passwords using modern algorithms (e.g. bcrypt, argon2)
   - Use unique salts per password
   - Never store or log plain-text passwords
   - Support password reset flows

4. **JWT Authentication**
   - Generate access tokens on successful login
   - Sign tokens with a secure secret or key pair
   - Include minimal, non-sensitive claims
   - Set appropriate expiration times
   - Support refresh token patterns when required

5. **Better Auth Integration**
   - Integrate Better Auth for standardized auth workflows
   - Use Better Auth adapters with the database layer
   - Configure providers, sessions, and callbacks correctly
   - Align Better Auth sessions with JWT or cookie-based auth

---

## Security Best Practices

- Always hash passwords before storing
- Use HTTPS-only cookies for auth tokens when applicable
- Protect routes with authentication middleware
- Rate-limit login and signup endpoints
- Avoid leaking auth errors (use generic messages)
- Rotate secrets and tokens periodically
- Follow OWASP authentication guidelines

---

## Recommended Flow

1. User submits signup form
2. Server validates input
3. Password is hashed and stored
4. User signs in with credentials
5. Server verifies hash
6. JWT or session is issued
7. Protected routes validate token/session
8. Logout invalidates session or token

---

## Example: Signup & Login Flow (Pseudo-Code)

```ts
// Signup
const hashedPassword = await hash(password);
await db.user.create({
  email,
  password: hashedPassword,
});

// Login
const user = await db.user.findByEmail(email);
const isValid = await verify(password, user.password);

if (!isValid) throw new Error("Invalid credentials");

const token = createJWT({ userId: user.id });
return token;
