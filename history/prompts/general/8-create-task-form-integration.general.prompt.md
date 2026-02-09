---
id: 8
title: create-task-form-integration
stage: green
date: 2026-02-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-hackathon-upgrade
user: Claude Sonnet 4.5
command: sp.implement @skills/react-nextjs @skills/web-frontend @skills/api-integration
labels: [api-integration, react, nextjs, dashboard, task-creation]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - phase-2/frontend/app/dashboard/page.tsx
tests:
 - none
---

## Prompt

@skills/react-nextjs @skills/web-frontend @skills/api-integration

**Action: Execute Phase 2.4 - Implement Create Task Form (T018)**

The Dashboard is reading empty tasks correctly. Now we need the UI to CREATE tasks.

**Context:**
- Frontend: `phase-2/frontend`
- Backend API: `POST /tasks`
- Requirements: Form must support Title, Description, Priority (Enum), Status (Enum), Due Date.

**Instructions:**

1.  **Create Task Form Component (`phase-2/frontend/components/CreateTaskForm.tsx`):**
    * **State:** Manage local state for form fields.
    * **Fields:**
        * `Title` (Input, required).
        * `Description` (Textarea).
        * `Priority` (Select: Low, Medium, High). Default: Medium.
        * `Status` (Select: Todo, In Progress, Done). Default: Todo.
        * `Due Date` (Input type="datetime-local").
    * **Submission Logic:**
        * Call `api.post('/tasks', payload)`.
        * On success: Call a prop function `onTaskCreated()` to notify parent.
        * On error: Show alert or error message.
    * **Styling:** Use Tailwind CSS for a clean look (e.g., "Add Task" button opens a modal or expands a form).

2.  **Integrate into Dashboard (`phase-2/frontend/app/dashboard/page.tsx`):**
    * Import `<CreateTaskForm />`.
    * Place it above the `<TaskFilters />` or add a "New Task" button to toggle it.
    * **Refetch Logic:** When `onTaskCreated` is triggered, reload the tasks list (re-run the fetch function).

**Goal:** User should be able to click "Add Task", fill the rich form, and see the new task appear immediately in the list.

## Response snapshot

Updated the dashboard page to properly integrate the CreateTaskForm component with an onSuccess callback that triggers task refetching after successful task creation. The form is now positioned above the TaskFilters as required.

## Outcome

- ✅ Impact: Enhanced dashboard with proper task creation integration and automatic refetching
- 🧪 Tests: none
- 📁 Files: 1 file modified - dashboard page with updated integration
- 🔁 Next prompts: Testing and verification of full create flow
- 🧠 Reflection: Implementation properly connects form submission to data refetching

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable
- Prompt variant (if applicable): not applicable
- Next experiment (smallest change to try): test the create flow