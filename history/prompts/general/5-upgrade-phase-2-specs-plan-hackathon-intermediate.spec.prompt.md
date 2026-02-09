---
id: 5
title: upgrade-phase-2-specs-plan-hackathon-intermediate
stage: spec
date_iso: 2026-02-02
surface: agent
model: Claude Sonnet 4.5
feature: hackathon-upgrade
branch: 001-hackathon-upgrade
user: user
command: "@skills/spec-driven-dev @skills/software-architecture\n\n**Action: Upgrade Phase 2 Specs & Plan (Hackathon Intermediate Level)**\n\nWe need to align our project with the official \"Hackathon II\" documentation. Our current spec is too basic. We must upgrade `spec.md` and `plan.md` to include **Intermediate Level** features.\n\n**Context:**\n- Project: Phase 2 (Full Stack Todo App).\n- Source: Hackathon PDF (Intermediate Level Requirements).\n\n**Instructions:**\n\n1.  **UPDATE `phase-2/spec.md`:**\n    * **Database Schema (Task Model):**\n        * Change `status` from Boolean to **Enum** (`todo`, `in_progress`, `done`).\n        * Add `priority`: **Enum** (`low`, `medium`, `high`).\n        * Add `due_date`: **DateTime** (nullable).\n        * Add `description`: **Text** (nullable).\n        * *Note:* Keep `user_id` as TEXT (Foreign Key) to handle Better Auth IDs correctly.\n    * **API Specifications:**\n        * Update `GET /api/v1/tasks`:\n            * Add Query Params for Filtering: `?search=keyword`, `?status=done`, `?priority=high`.\n            * Add Query Params for Sorting: `?sort_by=due_date|priority|created_at` & `?order=asc|desc`.\n\n2.  **UPDATE `phase-2/plan.md`:**\n    * **Database Strategy:** Mention that Alembic migrations must handle the new Enums and Column additions.\n    * **Backend Architecture:** Update the API section to include \"Advanced Filtering & Sorting Logic\" in the GET endpoint.\n    * **Frontend Architecture:**\n        * Mention \"Rich Task Form\": Needs Select inputs (Priority/Status) and Date Picker.\n        * Mention \"Dashboard Features\": Search Bar and Filter Dropdowns.\n\n**Goal:** Ensure `spec.md` and `plan.md` act as the blueprint for a \"Winning Hackathon Submission\" before we generate the task list."
labels: ["specification", "planning", "hackathon", "upgrade"]
links:
  spec: "phase-2/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "phase-2/spec.md"
  - "phase-2/plan.md"
  - "phase-2/checklists/requirements.md"
tests_yaml:
  - "Validation of spec and plan updates completed"
  - "Quality checklist created and verified"
outcome: "Successfully updated the Phase 2 specification and plan documents to include intermediate-level features required for the Hackathon II submission. Updated the Task model with ENUM types for status and priority, added due_date and description fields, and enhanced API specifications with advanced filtering and sorting capabilities. Updated the plan with Alembic migration strategy and frontend architecture improvements."
evaluation: "The updates successfully transformed the basic spec into a comprehensive intermediate-level specification suitable for a winning hackathon submission. All required features were implemented according to the specifications."
prompt_text: "@skills/spec-driven-dev @skills/software-architecture\n\n**Action: Upgrade Phase 2 Specs & Plan (Hackathon Intermediate Level)**\n\nWe need to align our project with the official \"Hackathon II\" documentation. Our current spec is too basic. We must upgrade `spec.md` and `plan.md` to include **Intermediate Level** features.\n\n**Context:**\n- Project: Phase 2 (Full Stack Todo App).\n- Source: Hackathon PDF (Intermediate Level Requirements).\n\n**Instructions:**\n\n1.  **UPDATE `phase-2/spec.md`:**\n    * **Database Schema (Task Model):**\n        * Change `status` from Boolean to **Enum** (`todo`, `in_progress`, `done`).\n        * Add `priority`: **Enum** (`low`, `medium`, `high`).\n        * Add `due_date`: **DateTime** (nullable).\n        * Add `description`: **Text** (nullable).\n        * *Note:* Keep `user_id` as TEXT (Foreign Key) to handle Better Auth IDs correctly.\n    * **API Specifications:**\n        * Update `GET /api/v1/tasks`:\n            * Add Query Params for Filtering: `?search=keyword`, `?status=done`, `?priority=high`.\n            * Add Query Params for Sorting: `?sort_by=due_date|priority|created_at` & `?order=asc|desc`.\n\n2.  **UPDATE `phase-2/plan.md`:**\n    * **Database Strategy:** Mention that Alembic migrations must handle the new Enums and Column additions.\n    * **Backend Architecture:** Update the API section to include \"Advanced Filtering & Sorting Logic\" in the GET endpoint.\n    * **Frontend Architecture:**\n        * Mention \"Rich Task Form\": Needs Select inputs (Priority/Status) and Date Picker.\n        * Mention \"Dashboard Features\": Search Bar and Filter Dropdowns.\n\n**Goal:** Ensure `spec.md` and `plan.md` act as the blueprint for a \"Winning Hackathon Submission\" before we generate the task list."
response_text: "Successfully updated the Phase 2 specification and plan documents to include intermediate-level features required for the Hackathon II submission. Updated the Task model with ENUM types for status and priority, added due_date and description fields, and enhanced API specifications with advanced filtering and sorting capabilities. Updated the plan with Alembic migration strategy and frontend architecture improvements."
---

# PHR-5: Upgrade Phase 2 Specs & Plan (Hackathon Intermediate Level)

## Summary
Updated Phase 2 specification and plan documents to include intermediate-level features required for Hackathon II submission.

## Changes Made

### spec.md Updates:
- Updated Task Model to use ENUM types for `status` ('todo', 'in_progress', 'done') and `priority` ('low', 'medium', 'high')
- Added `due_date` TIMESTAMP field (nullable) to Task model
- Enhanced API specifications with advanced filtering and sorting parameters for GET /api/v1/tasks:
  - Query parameters: `?search=keyword`, `?status=todo|in_progress|done`, `?priority=low|medium|high`
  - Sorting parameters: `?sort_by=due_date|priority|created_at`, `?order=asc|desc`

### plan.md Updates:
- Added Alembic Migration Strategy section to handle ENUM types and column additions
- Added Advanced Filtering & Sorting Logic section to Backend Architecture
- Added Rich Task Form Implementation section with Select dropdowns and Date picker
- Added Dashboard Features section with Search bar and Filter dropdowns

### Additional:
- Created specification quality checklist at phase-2/checklists/requirements.md
- All updates align with Hackathon II intermediate level requirements

## Verification
- All required features implemented according to specifications
- Specification quality checklist completed and verified
- Ready for next phase of development planning