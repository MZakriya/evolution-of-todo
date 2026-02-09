---
id: 1
title: "Create Phase 2 Spec"
stage: "spec"
date_iso: "2026-01-31"
surface: "agent"
model: "Claude Sonnet 4.5"
feature: "phase-2-spec"
branch: "main"
user: "user"
command: "/sp.specify"
labels: ["specification", "full-stack", "todo-app"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files_yaml: |
  - "phase-2/spec.md"
  - "phase-2/checklists/requirements.md"
tests_yaml: |
  - "spec-validation"
prompt_text: |
  @skills/spec-driven-dev @skills/software-architecture

  **Action: Create Phase 2 Specification Document**

  We are restarting Phase 2 (Full Stack Todo App) from scratch to ensure a clean architecture. We need a comprehensive `phase-2/spec.md` file.

  **Context:**
  - Root Dir: `phase-2/`
  - Backend: FastAPI (Async), SQLModel, Alembic, Asyncpg.
  - Frontend: Next.js 15+ (App Router), Tailwind CSS, Lucide React.
  - Database: Neon Serverless Postgres.
  - Auth: Better Auth (handling User/Session management).

  **Instructions:**

  1.  **Create `phase-2/spec.md`** with the following sections:

      * **1. Architecture Overview:**
          * Hybrid approach: Better Auth manages the `User` table directly in Postgres. Backend reads `User` table via Foreign Keys but does NOT write/manage auth credentials.

      * **2. Database Schema (Critical):**
          * **User Model:** Must match Better Auth defaults. **ID must be TEXT (String)**, not Integer. Fields: `id`, `name`, `email`, `emailVerified`, `image`, `createdAt`, `updatedAt`.
          * **Task Model:** Fields: `id` (int/serial), `title`, `description`, `status`, `priority`, `user_id` (TEXT, Foreign Key to User.id).

      * **3. Backend Specifications:**
          * **Tech:** FastAPI, Uvicorn, Pydantic.
          * **DB Connection:** Use `asyncpg`. **Must explicitly handle SSL (`sslmode=require`)** to avoid Neon connection errors.
          * **Auth Middleware:** Custom dependency to verify JWT tokens issued by Better Auth (using `better-auth` server-side helper or manual JWT verification).

      * **4. Frontend Specifications:**
          * **Tech:** Next.js, Shadcn/UI (or raw Tailwind components).
          * **Auth Client:** Use `@better-auth/react` (specifically the React hooks `useSession`, `signIn`, `signUp`) to avoid "hook not found" errors.
          * **API Client:** Axios/Fetch wrapper that automatically attaches the Bearer token.

      * **5. Project Structure:**
          * `backend/` (FastAPI app)
          * `frontend/` (Next.js app)

      * **6. Environment Variables:**
          * List required variables for both Backend (`DATABASE_URL`, `SECRET_KEY`) and Frontend (`NEXT_PUBLIC_API_URL`, `BETTER_AUTH_URL`, `BETTER_AUTH_SECRET`).

  **Goal:** This spec should serve as the "Source of Truth" to prevent previous issues like Integer/String ID mismatches and SSL handshake failures.
response_text: |
  Successfully created comprehensive Phase 2 specification document (phase-2/spec.md) with all required sections:
  - Architecture Overview with hybrid Better Auth approach
  - Database Schema with proper TEXT ID types for User model and Foreign Key relationships
  - Backend specifications with FastAPI, asyncpg, and SSL requirements
  - Frontend specifications with Next.js and @better-auth/react integration
  - Complete project structure layout
  - Environment variables for both backend and frontend
  - User scenarios, functional requirements, success criteria and constraints
outcome: "spec created successfully and validated"
evaluation: "complete"
---

# PHR: Create Phase 2 Spec

## Summary

Successfully created the Phase 2 Full Stack Todo App specification document with all required sections and components as specified in the feature requirements.

## Details

The specification document includes:
- Architecture overview with hybrid Better Auth approach
- Database schema with proper TEXT ID types for User model
- Backend specifications with FastAPI and SSL requirements
- Frontend specifications with Next.js and authentication integration
- Complete project structure layout
- Environment variables for both backend and frontend
- User scenarios and functional requirements
- Success criteria and constraints

The spec addresses the critical requirements to prevent previous issues like Integer/String ID mismatches and SSL handshake failures.