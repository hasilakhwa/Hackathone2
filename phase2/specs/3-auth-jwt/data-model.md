# Data Model: JWT Authentication System

## Entity: JWT Token

### Claims Structure:
- **sub** (Subject): User identifier (equivalent to user_id)
- **email**: User's email address for identification
- **iat** (Issued At): Unix timestamp when token was issued
- **exp** (Expiration): Unix timestamp when token expires
- **jti** (JWT ID): Unique identifier for token (optional, for revocation)

### Validation Rules:
- Token signature must be valid against BETTER_AUTH_SECRET
- exp claim must not be in the past
- iat claim must not be in the future
- sub claim must correspond to a valid user in the system

### State Transitions:
- Issued (during login/signup) → Active → Expired/Revoked

## Entity: User Identity (from JWT claims)

### Attributes:
- **user_id**: Integer identifier extracted from JWT sub claim
- **email**: String email extracted from JWT email claim
- **is_authenticated**: Boolean indicating if user has valid JWT

### Relationships:
- Links to existing User model from previous specifications
- Provides authentication context for API requests

## Entity: Authorization Context

### Attributes:
- **authenticated_user_id**: User ID extracted from validated JWT
- **permissions**: Access rights granted based on user role
- **request_scopes**: Valid scopes for the current request

### Validation Rules:
- Must have valid JWT to establish context
- User ID in context must match user ID in API endpoint path
- Permissions must be verified for each protected resource

## Entity: Authentication Session

### Attributes:
- **session_id**: Optional session identifier for state management
- **user_id**: Associated user identifier
- **expires_at**: Timestamp for session expiration
- **last_activity**: Timestamp of last activity for session management

### State Transitions:
- Created (on successful authentication) → Active → Expired/Revoked

## Security Constraints:

### Token Integrity:
- All JWT tokens must be signed with HS256 algorithm
- Signature verification required for all API requests
- Tampered tokens must result in immediate rejection

### User Isolation:
- User ID from JWT must match user ID in URL path for protected endpoints
- Requests with mismatched user IDs must return 403 Forbidden
- Cross-user data access must be prevented at the application layer

### Expiration Handling:
- Tokens with expired exp claim must be rejected with 401
- Short-lived tokens preferred for security (7 days default)
- Refresh mechanisms should be implemented for extended sessions