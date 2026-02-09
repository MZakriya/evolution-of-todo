---
id: 3
title: "Strategic Dev Plan"
stage: "plan"
date_iso: "2026-01-31"
surface: "agent"
model: "Claude Sonnet 4.5"
feature: "phase-2-spec"
branch: "main"
user: "user"
command: "/sp.plan"
labels: ["architecture", "strategic-planning", "full-stack"]
links:
  spec: "phase-2/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files_yaml: |
  - "phase-2/plan.md"
tests_yaml: |
  - "strategic-plan-review"
prompt_text: |
  @skills/spec-driven-dev @skills/software-architecture

  **Action: Create Strategic Development Plan (plan.md)**

  The previous attempt at `plan.md` was just a list of tasks. We need a proper **Strategic Plan** that explains the *Architecture* and *Integration Logic* before we generate the task list.

  **Context:**
  - Project: Todo App (Reboot Phase 2).
  - Goal: Fix SSL issues, ID mismatches (Int vs String), and Auth loops.

  **Instructions:**

  1.  **Overwrite `phase-2/plan.md`** with the following High-Level Strategy sections:

      * **1. Database Strategy (The Foundation):**
          * Explain the "Hybrid Auth" approach: Better Auth owns the User table, Backend owns the Task table.
          * **Critical Decision:** Explicitly state that `User.id` MUST be `TEXT` to prevent the "Integer Mismatch" error.
          * **Connection Logic:** Explain using `asyncpg` with `ssl: require` to handle Neon DB securely.

      * **2. Backend Architecture:**
          * Describe the API structure (`/api/v1`).
          * **Auth Flow:** How the Backend will verify the JWT token sent by the Frontend (Stateless verification).
          * **Error Handling:** Standardized error responses (401 vs 403 vs 404).

      * **3. Frontend Architecture:**
          * **Client-Side Auth:** Explain using `@better-auth/react` hooks (`useSession`) to avoid the "Function not found" error.
          * **API Client Layer:** Describe a centralized `api.ts` that intercepts requests and injects the `Bearer` token automatically.
          * **State Management:** Using simple React State + SWR/TanStack Query (optional) or just `useEffect` for fetching.

      * **4. Integration & Verification Strategy:**
          * Define "Checkpoints":
              * Checkpoint A: DB connects and Tables exist (Manual Script).
              * Checkpoint B: API returns 401 for unauthenticated requests (Swagger).
              * Checkpoint C: Frontend can Login/Signup (Better Auth).
              * Checkpoint D: Frontend displays Tasks from Backend.

  **Format:** Use narrative text and bullet points for strategy. **DO NOT use "T001" or checkbox lists here.** (That belongs in `tasks.md`).

  **Goal:** A document that any developer can read to understand *HOW* the system works, not just *WHAT* to type.
response_text: |
  Successfully created a strategic development plan that explains the architecture and integration logic:
  - Database Strategy with Hybrid Auth approach and TEXT ID decision
  - Backend Architecture with API structure, auth flow, and error handling
  - Frontend Architecture with Better Auth integration and API client layer
  - Integration & Verification Strategy with four checkpoints
  The plan now explains the "HOW" rather than just the "WHAT" and provides architectural context for developers.
outcome: "strategic plan created with architectural context"
evaluation: "complete"
---
# PHR: Strategic Dev Plan

## Summary

Successfully transformed the Phase 2 plan from a task list into a strategic development plan that explains architecture and integration logic.

## Details

The strategic plan now includes:
- Database Strategy with Hybrid Auth approach and critical TEXT ID decision
- Backend Architecture with API structure, stateless auth flow, and standardized error handling
- Frontend Architecture with Better Auth React integration and centralized API client
- Integration & Verification Strategy with progressive checkpoints
- Success metrics to validate the architectural decisions