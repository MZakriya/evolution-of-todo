---
id: 0007
title: Frontend Feature Implementation Dashboard Task List Create Form
stage: green
date: 2026-01-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: unspecified
command: /sp.implement
labels: ["frontend", "dashboard", "task-management", "react", "nextjs"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - phase-2/frontend/lib/api.ts
 - phase-2/frontend/app/dashboard/page.tsx
 - phase-2/frontend/components/TaskCard.tsx
 - phase-2/frontend/components/CreateTaskForm.tsx
 - phase-2/tasks.md
tests:
 - none
---

## Prompt

@skills/spec-driven-dev @skills/react-nextjs @skills/web-frontend

**Action: Execute Frontend Feature Implementation (Tasks T032, T033, T034)**

Authentication is set up. Now we need to implement the main **Dashboard**, **Task List**, and **Create Task Form**.

**Context:**
- Frontend: `phase-2/frontend/`
- Backend API: `http://localhost:8000/api`
- Auth: Better Auth (Client already configured).

**Instructions:**

1.  **Update API Client (T028 Refinement):**
    -   Edit `phase-2/frontend/lib/api.ts`.
    -   Add a function to retrieve the Token from the Auth Session (using `authClient.getSession()`).
    -   Ensure `fetch` requests automatically attach `Authorization: Bearer <token>` header if a session exists.

2.  **Create Dashboard Page (T032, T033):**
    -   Create `phase-2/frontend/app/dashboard/page.tsx`.
    -   **Protection:** Check if user is logged in. If not, redirect to `/login`.
    -   **Data Fetching:** Use `useEffect` to call `api.getTasks()` on load.
    -   **UI:** Display a Welcome message ("Hello, {user.name}") and the list of tasks.

3.  **Create Task Components (T034):**
    -   Create `phase-2/frontend/components/TaskCard.tsx`:
        -   Display Title, Description, Priority (colored badge), Status.
        -   Add "Delete" and "Complete" buttons (UI only for now).
    -   Create `phase-2/frontend/components/CreateTaskForm.tsx`:
        -   Form with Title, Description, Priority (Select).
        -   On Submit: Call `api.createTask()`, then refresh the Dashboard list.

4.  **Wire Everything Up:**
    -   Import `CreateTaskForm` and `TaskCard` into the Dashboard page.
    -   Ensure the list updates immediately after adding a new task.

**Post-Execution:**
-   Update `phase-2/tasks.md`: Mark **[x] T032, T033, T034** as complete.
-   **Verification:** User should be able to Login, go to Dashboard, Add a Task, and see it appear in the list.

## Response snapshot

Successfully implemented the frontend dashboard, task list, and create task form with authentication protection and real-time updates.

## Outcome

- ✅ Impact: Completed dashboard page with authentication protection, task list display, and create form; implemented TaskCard and CreateTaskForm components with full functionality; updated API client with task-specific methods
- 🧪 Tests: none
- 📁 Files: phase-2/frontend/lib/api.ts, phase-2/frontend/app/dashboard/page.tsx, phase-2/frontend/components/TaskCard.tsx, phase-2/frontend/components/CreateTaskForm.tsx, phase-2/tasks.md
- 🔁 Next prompts: none
- 🧠 Reflection: Well-structured implementation following Next.js best practices with proper authentication integration and real-time UI updates

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): None needed