
```markdown
---
name: nextjs-task-form-component
description: Create form component for adding/editing tasks with validation. Use in create/edit modals or pages.
---

# Task Form Component (Next.js)

## Instructions

1. **Fields**
   - Title (required)
   - Description (textarea)
   - Submit button

2. **Submission**
   - POST to /api/{user_id}/tasks or PUT for edit
   - Use apiFetch

3. **Validation**
   - Client-side with React Hook Form or native

## Best Practices
- Accessibility (labels, aria)
- Loading state on submit
- Success toast / redirect
- Error display

## Example Structure

```tsx
// components/TaskForm.tsx
"use client";
import { useForm } from "react-hook-form";
import { apiFetch } from "@/lib/api";

type TaskFormData = { title: string; description?: string };

export default function TaskForm({ userId }: { userId: string }) {
  const { register, handleSubmit } = useForm<TaskFormData>();

  const onSubmit = async (data: TaskFormData) => {
    await apiFetch(`/api/${userId}/tasks`, {
      method: "POST",
      body: JSON.stringify(data),
    });
    // refresh or toast
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <input {...register("title", { required: true })} placeholder="Task title" className="border p-2 w-full" />
      <textarea {...register("description")} placeholder="Details..." className="border p-2 w-full" />
      <button type="submit" className="bg-blue-500 text-white p-2">Add Task</button>
    </form>
  );
}