# Claude Code Agent Context: Backend API & Data Layer

## Project Context
- Project: Todo Full-Stack Web Application
- Feature: Backend API & Data Layer (001-backend-api-data)
- Architecture: FastAPI backend with JWT authentication
- Database: Neon Serverless PostgreSQL with SQLModel ORM

## Technology Stack
- Language: Python 3.11
- Framework: FastAPI
- ORM: SQLModel
- Database: PostgreSQL (via Neon)
- Authentication: JWT token verification

## Key Directories
- backend/src/: Main source code
- backend/src/models/: Data models using SQLModel
- backend/src/api/: API route definitions
- backend/src/services/: Business logic
- backend/src/core/: Configuration and security utilities

## Critical Requirements
- All API endpoints must validate JWT tokens
- User data isolation must be enforced at database level
- FastAPI dependencies should handle authentication
- SQLModel models must include proper relationships
- Error responses must follow HTTP standards