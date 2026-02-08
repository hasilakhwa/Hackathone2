
```markdown
---
name: nextjs-task-list-page
description: Build the main task list page in Next.js with fetch, display, and actions (complete/delete). Use for UI task management.
---

# Next.js Task List Page

## Instructions

1. **Server component**
   - Fetch tasks using apiFetch with user_id from session

2. **UI**
   - Table or cards for tasks
   - Checkbox for complete toggle
   - Delete button

3. **Interactivity**
   - Use optimistic updates or revalidate on actions

## Best Practices
- Use suspense/loading states
- Handle empty state
- Mobile responsive grid
- Error boundary if fetch fails

## Example Structure

```tsx
// app/tasks/page.tsx
import { getSession } from "@/lib/auth";
import { apiFetch } from "@/lib/api";
import TaskItem from "@/components/TaskItem";

export default async function TasksPage() {
  const session = await getSession();
  if (!session?.user) redirect("/login");

  const tasks = await apiFetch(`/api/${session.user.id}/tasks`);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl mb-4">My Tasks</h1>
      {tasks.length === 0 ? (
        <p>No tasks yet. Create one!</p>
      ) : (
        <ul className="space-y-2">
          {tasks.map((task) => (
            <TaskItem key={task.id} task={task} />
          ))}
        </ul>
      )}
    </div>
  );
}