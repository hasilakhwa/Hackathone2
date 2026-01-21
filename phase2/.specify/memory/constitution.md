<!--
Sync Impact Report:
Version change: N/A → 1.0.0
List of modified principles: N/A → Agentic-First Development, No Manual Coding, Separation of Concerns, Security-by-Design, Production-Grade Structure
Added sections: Core Principles (6), Additional Constraints, Development Workflow, Governance
Removed sections: None
Templates requiring updates: ✅ Updated all relevant sections
Follow-up TODOs: None
-->
# Todo Full-Stack Web Application Constitution

## Core Principles

### I. Agentic-First Development
Agentic-first development (spec → plan → tasks → implementation) with Claude Code as the primary implementation mechanism. All code must be generated through the agentic workflow without manual intervention. This ensures reproducible, auditable, and consistent development outcomes.

### II. No Manual Coding
No manual coding is allowed - all code must be generated via Claude Code following the Agentic Dev Stack methodology. This enforces strict adherence to the spec-driven approach and eliminates ad-hoc implementations that deviate from the planned architecture.

### III. Clear Separation of Concerns
Clear separation of concerns across specifications (Backend, Auth, Frontend) with well-defined interfaces and minimal coupling. Each layer must operate independently while maintaining consistent data contracts and API boundaries to enable parallel development and testing.

### IV. Security-by-Design
Security-by-design principles with authentication enforced at every layer of the application stack. Security measures must be implemented from the ground up rather than added as an afterthought, ensuring that all data access, user validation, and system interactions follow security best practices.

### V. Production-Grade Structure
Production-grade structure must be maintained despite hackathon scope, with proper error handling, logging, monitoring capabilities, and operational readiness built into the application from the start. This ensures the codebase can evolve beyond the hackathon phase.

### VI. Traceability and Accountability
Every feature must be traceable to an explicit requirement and every API endpoint must map to a documented behavior. This ensures that all functionality serves a defined purpose and can be validated against specific acceptance criteria.

## Additional Constraints

### Technology Stack Requirements
- Frontend: Next.js 16+ using App Router for modern React development
- Backend: Python FastAPI for high-performance API development
- ORM: SQLModel for unified data modeling across SQLAlchemy and Pydantic
- Database: Neon Serverless PostgreSQL for scalable, managed database service
- Authentication: Better Auth (JWT-based) for secure, standardized authentication
- Auth secret shared via BETTER_AUTH_SECRET environment variable for secure credential management

### Security Standards
- All API endpoints require a valid JWT token after authentication to prevent unauthorized access
- Requests without a token must return 401 Unauthorized status code to enforce security boundaries
- Backend must validate JWT signature and expiration to prevent token replay and expired access
- User ID must be derived from JWT, not trusted from client input to prevent ID spoofing
- Task ownership must be enforced on every CRUD operation to maintain data isolation
- No cross-user data access under any circumstances to protect user privacy and data integrity

### API Standards
- RESTful conventions must be followed to ensure predictable and standardized API behavior
- HTTP methods must match intent (GET, POST, PUT, PATCH, DELETE) for semantic clarity
- Consistent JSON response shapes for reliable client-server communication
- Proper HTTP status codes for success and failure cases to enable proper error handling
- Clear error messages without leaking sensitive data to prevent information disclosure

### Frontend Standards
- Responsive UI across desktop and mobile to ensure accessibility across devices
- Auth-aware routing (protected vs public pages) to enforce security boundaries
- API client must automatically attach JWT token to ensure seamless authentication
- Loading, error, and empty states must be handled explicitly to provide good user experience
- UI must reflect backend truth (no fake optimistic state) to maintain data consistency

## Development Workflow

### Agentic Workflow Rules
- Each spec must have its own sp.specify prompt to ensure comprehensive requirement coverage
- Each sp.specify must result in a concrete execution plan to guide implementation
- Plans must be broken into deterministic, testable tasks to enable incremental delivery
- No implementation before plan approval to ensure architectural alignment
- Iteration is allowed, silent deviation is not to maintain project integrity

### Documentation & Evaluation Readiness
- Specs must be readable by judges without extra context to ensure clear communication
- Plans must clearly show reasoning and ordering to demonstrate thoughtful design
- Decisions must be explicit, not implied to enable proper review and validation
- Tradeoffs must be stated when relevant to document design considerations

### Success Criteria
- All 5 Basic Level features implemented as a working web app to satisfy functional requirements
- Multi-user task isolation verified end-to-end to ensure proper data separation
- JWT authentication works across frontend and backend to provide secure access control
- Backend persists data correctly in Neon PostgreSQL to ensure data reliability
- Frontend fully functional using generated code only to validate agentic approach
- Entire workflow demonstrates proper Agentic Dev Stack usage to achieve methodological goals

## Governance

This constitution supersedes all other development practices and guidelines for the Todo Full-Stack Web Application project. All team members must comply with these principles during the hackathon phase.

Amendments to this constitution require explicit documentation of the change, approval from the project lead, and a migration plan for any affected components. All pull requests and code reviews must verify compliance with these constitutional principles before merging.

The development team must conduct periodic compliance reviews to ensure ongoing adherence to these principles, with special attention to security standards and agentic workflow requirements.

**Version**: 1.0.0 | **Ratified**: 2026-01-20 | **Last Amended**: 2026-01-20
