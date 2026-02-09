---
id: 2
title: "Phase 2 Dev Plan"
stage: "plan"
date_iso: "2026-01-31"
surface: "agent"
model: "Claude Sonnet 4.5"
feature: "phase-2-spec"
branch: "main"
user: "user"
command: "/sp.plan"
labels: ["planning", "full-stack", "todo-app"]
links:
  spec: "phase-2/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files_yaml: |
  - "phase-2/plan.md"
tests_yaml: |
  - "plan-validation"
prompt_text: |
  @skills/spec-driven-dev @skills/project-planning

  **Action: Create Phase 2 Development Plan**

  Based on the newly created `phase-2/spec.md`, we need a step-by-step execution plan stored in `phase-2/plan.md`.

  **Context:**
  - We are rebooting the project to fix previous architecture issues (SSL, Integer vs String IDs, Auth Loops).
  - The plan must be sequential and testable at each stage.

  **Instructions:**

  1.  **Read `phase-2/spec.md`** to ensure alignment.

  2.  **Create `phase-2/plan.md`** with the following logical phases:

      * **Phase 2.1: Backend Foundation & Database (The Bedrock)**
          * Setup FastAPI, Env (`DATABASE_URL`), and `asyncpg` with explicit SSL.
          * Define Models: `User` (Text ID mandatory) and `Task`.
          * Alembic Setup: Generate migrations for both tables.
          * **Verification:** Run a script to confirm DB connection and table creation before moving on.

      * **Phase 2.2: Backend API Implementation**
          * Create Auth Dependency (Verify Bearer Token).
          * Implement `POST /tasks` and `GET /tasks`.
          * Implement `PUT` and `DELETE`.
          * **Verification:** Test via Swagger UI using a dummy token.

      * **Phase 2.3: Frontend Setup & Auth Integration**
          * Init Next.js + Tailwind.
          * Setup Better Auth with **React Client** (Fixing the "hook not found" issue).
          * Create Login/Signup Pages.
          * **Verification:** Successfully create a user in DB (verify ID is a String).

      * **Phase 2.4: Full Integration (Dashboard)**
          * Build API Client (Auto-attach Token).
          * Create Dashboard (List Tasks).
          * Create Task Form.
          * **Verification:** Full flow: Login -> Dashboard -> Create Task -> View Task.

  3.  **Format:** Use Markdown checklists (`- [ ]`) for every step so we can track progress in `tasks.md` later.

  **Goal:** A bulletproof roadmap that prevents the previous "Redirect Loop" and "Schema Mismatch" errors.
response_text: |
  Successfully created the Phase 2 development plan (phase-2/plan.md) with all required phases and tasks:
  - Phase 2.1: Backend Foundation & Database (T001-T005)
  - Phase 2.2: Backend API Implementation (T006-T011)
  - Phase 2.3: Frontend Setup & Auth Integration (T012-T016)
  - Phase 2.4: Full Integration (Dashboard) (T017-T021)
  All tasks include verification steps to ensure each component works before moving to the next phase, addressing the key issues from the specification.
outcome: "plan created successfully with verification checkpoints"
evaluation: "complete"
---
# PHR: Phase 2 Dev Plan

## Summary

Successfully created the Phase 2 development plan with sequential phases and verification checkpoints to prevent previous architecture issues.

## Details

The plan includes four main phases:
- Backend Foundation & Database (The Bedrock)
- Backend API Implementation
- Frontend Setup & Auth Integration
- Full Integration (Dashboard)

Each phase includes specific tasks with verification steps to ensure proper implementation of critical components like SSL handling, correct ID types, and authentication integration.