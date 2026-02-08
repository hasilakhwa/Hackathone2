---
id: 1
title: create-frontend-auth-plan
stage: plan
date_iso: 2026-02-06
surface: agent
model: claude-haiku-4-5-20251001
feature: frontend-auth
branch: 1-frontend-auth
user: user
command: /sp.plan "Build fresh Next.js frontend with Better Auth and professional Todo UI..."
labels: ["frontend", "authentication", "plan", "nextjs", "better-auth"]
links:
  spec: ../specs/1-frontend-auth/spec.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - specs/1-frontend-auth/plan.md
  - specs/1-frontend-auth/research.md
  - specs/1-frontend-auth/data-model.md
  - specs/1-frontend-auth/contracts/api-contracts.md
  - specs/1-frontend-auth/quickstart.md
  - .specify/memory/claude-agent-context.md
tests_yaml:
  - specs/1-frontend-auth/plan.md reviewed for completeness
  - API contracts validated against feature requirements
  - Data model validated against feature requirements
outcome: Implementation plan created with all supporting artifacts
evaluation: Success
---

# PHR: create-frontend-auth-plan

## Original Prompt

Build fresh Next.js frontend with Better Auth and professional Todo UI

Technical choices:
- Create project: User runs "npx create-next-app@latest" → choose TypeScript, Tailwind, App Router
- Folder: Work only inside the newly created project folder
- Auth: Better Auth (jwt plugin), server config in lib/auth.ts, routes in app/api/auth/[...all]/route.ts
- Client: better-auth/client with jwtClient()
- API client: lib/api.ts – fetch wrapper with token from session
- Styling: Tailwind + optional shadcn/ui (Button, Card, Input, Checkbox, Toast)
- Animations: Framer Motion (fade-in, scale hover)
- Layout: Root layout with navbar (logout button after login)
- Protected: Use middleware.ts or layout check for session
- Env: .env.local – BETTER_AUTH_SECRET (same as backend), NEXT_PUBLIC_API_URL

Steps outline:
1. User creates fresh project: npx create-next-app@latest (name e.g. todo-frontend)
2. Install dependencies: better-auth, @better-auth/client, framer-motion, sonner (toast), optional shadcn/ui
3. Configure Better Auth: lib/auth.ts with jwt(), shared secret
4. Set up auth routes: app/api/auth/[...all]/route.ts
5. Create client helpers: useSession, getAccessToken
6. API wrapper: lib/api.ts – add Authorization: Bearer ${token}
7. Pages: app/login/page.tsx, app/signup/page.tsx (simple forms)
8. Protected dashboard: app/tasks/page.tsx – fetch tasks, display cards, add form
9. Components: TaskCard (checkbox, delete), TaskForm, Navbar
10. Middleware or layout: Redirect if no session on /tasks
11. Add loading/error states + toasts for feedback
12. Test: npm run dev → signup → login → tasks page

Output artifacts expected:
- app/layout.tsx (with navbar)
- app/login/page.tsx, app/signup/page.tsx
- app/tasks/page.tsx
- components/Navbar.tsx, components/TaskCard.tsx, components/TaskForm.tsx
- lib/auth.ts, lib/api.ts
- middleware.ts (optional for protection)
- .env.local template comments

## Response Summary

Successfully created a comprehensive implementation plan for the Next.js frontend with Better Auth integration. The plan includes:

- Technical Context detailing all technologies and approaches
- System, Component, and Data Architecture definitions
- Detailed Development Plan with 6 phases
- Risk Assessment and mitigation strategies
- Success Criteria aligned with requirements

Supporting artifacts were also created:
- Research document with technical decisions and rationale
- Data model defining User, Task, and Session entities
- API contracts specifying all required endpoints
- Quickstart guide for project setup
- Agent context file with technology details

## Files Created

- specs/1-frontend-auth/plan.md: Main implementation plan
- specs/1-frontend-auth/research.md: Technical research and decisions
- specs/1-frontend-auth/data-model.md: Data architecture
- specs/1-frontend-auth/contracts/api-contracts.md: API specifications
- specs/1-frontend-auth/quickstart.md: Setup guide
- .specify/memory/claude-agent-context.md: Technology context