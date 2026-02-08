# Quickstart Guide: Next.js Frontend for Multi-User Todo App

## Prerequisites
- Node.js 18+ installed
- Access to backend API service
- GIT version control

## Setup Instructions

### 1. Clone or Create Project
```bash
npx create-next-app@latest todo-frontend
cd todo-frontend
```

### 2. Install Dependencies
```bash
npm install better-auth @better-auth/client framer-motion sonner
# Optional: Install shadcn/ui components
# npx shadcn-ui@latest add button card input checkbox toast
```

### 3. Environment Configuration
Create `.env.local` file in project root:
```env
BETTER_AUTH_SECRET=your-unique-secret-string
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 4. Initialize Better Auth
Create `lib/auth.ts`:
```typescript
import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
  plugins: [
    jwt({
      secret: process.env.BETTER_AUTH_SECRET || "",
    })
  ],
  // Additional auth configuration...
});
```

### 5. Create Auth API Routes
Create `app/api/auth/[...all]/route.ts`:
```typescript
import { auth } from "@/lib/auth";

export const { GET, POST } = auth.$authorization();
```

### 6. Start Development Server
```bash
npm run dev
```

## Key Features
- User registration and authentication
- Protected routes for task management
- Task creation, viewing, updating, and deletion
- Responsive UI with mobile-first design
- Professional styling with Tailwind CSS
- JWT-based authentication

## Next Steps
1. Implement the UI components (navbar, task cards, forms)
2. Connect to backend API for task operations
3. Add animations with Framer Motion
4. Test authentication flow
5. Verify responsive design on different devices