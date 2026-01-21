---
name: backend-routes
description: Generate backend routes, handle HTTP requests/responses, and connect to databases efficiently. Use for building API endpoints and server logic.
---

# Backend Skill: Routes & DB Handling

## Instructions

1. **Route Creation**
   - Define RESTful routes (GET, POST, PUT, DELETE)
   - Use clear and consistent route naming
   - Group related routes logically (e.g., `/users`, `/products`)

2. **Request Handling**
   - Parse incoming request data (query, params, body)
   - Validate input and return proper error responses
   - Implement middleware for authentication, logging, or validation

3. **Response Handling**
   - Send structured JSON responses
   - Include proper HTTP status codes
   - Handle errors gracefully with meaningful messages

4. **Database Integration**
   - Connect to relational (MySQL, PostgreSQL) or NoSQL (MongoDB) databases
   - Perform CRUD operations securely
   - Use parameterized queries or ORM methods to prevent injection
   - Handle asynchronous DB operations correctly

## Best Practices
- Keep route handlers small and modular
- Use middleware for repetitive tasks
- Follow REST conventions for HTTP methods and status codes
- Validate and sanitize all input data
- Ensure proper error handling and logging

## Example Structure (Express.js)
```javascript
const express = require('express');
const router = express.Router();
const db = require('./db');

// GET all users
router.get('/users', async (req, res) => {
  try {
    const users = await db.getUsers();
    res.status(200).json(users);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
});

// POST create a new user
router.post('/users', async (req, res) => {
  const { name, email } = req.body;
  try {
    const newUser = await db.createUser({ name, email });
    res.status(201).json(newUser);
  } catch (error) {
    res.status(400).json({ message: 'Invalid data' });
  }
});

module.exports = router;
