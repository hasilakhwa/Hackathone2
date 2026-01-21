---
name: frontend-layout
description: Build responsive pages, components, and layouts with clean styling. Use for modern web UI development.
---

# Frontend Layout & Component Design

## Instructions

1. **Page Structure**
   - Use semantic HTML elements (`<header>`, `<main>`, `<footer>`, `<section>`)
   - Ensure responsive layout with CSS Grid or Flexbox
   - Maintain consistent spacing and alignment

2. **Components**
   - Buttons, cards, modals, navigation bars
   - Reusable component structure
   - Props-driven or state-aware (for dynamic behavior)

3. **Styling**
   - Mobile-first approach
   - Use utility classes (Tailwind, CSS modules, or styled-components)
   - Maintain consistent color palette, typography, and spacing

4. **Accessibility**
   - Ensure semantic markup
   - Provide ARIA attributes where needed
   - Keyboard navigable elements

## Best Practices
- Keep components small and reusable
- Avoid inline styles; separate styling logic
- Use descriptive class names or CSS modules
- Ensure high contrast and readable typography

## Example Structure
```html
<section class="page-section">
  <div class="container mx-auto px-4">
    <header class="flex justify-between items-center py-4">
      <h1 class="text-2xl font-bold">Page Title</h1>
      <nav>
        <ul class="flex gap-4">
          <li><a href="#" class="hover:underline">Home</a></li>
          <li><a href="#" class="hover:underline">About</a></li>
        </ul>
      </nav>
    </header>

    <main class="my-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="card p-4 shadow-md rounded">
          <h2 class="text-xl font-semibold">Card Title</h2>
          <p>Card description goes here.</p>
          <button class="btn-primary mt-2">Action</button>
        </div>
      </div>
    </main>

    <footer class="py-4 text-center text-sm text-gray-500">
      © 2026 Your Company
    </footer>
  </div>
</section>
