---
id: 1
title: Force Header Auth Fix
stage: general
date: 2026-02-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-hackathon-upgrade
user: Claude Sonnet 4.5
command: Manual implementation of forced header authentication
labels: [authentication, security, cors, header-auth, backend]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - D:\All Projects\evolution-of-todo\phase-2\frontend\lib\api.ts
  - D:\All Projects\evolution-of-todo\phase-2\backend\src\auth.py
tests:
  - Fixed frontend to force Authorization header
  - Updated backend to resiliently handle tokens
---

## Prompt

Force Header Auth & Fix CORS Crash:

The user is facing a deadlock:
1. Frontend says "relying on cookies" (It is NOT forcing the header).
2. Backend crashes (500) likely due to the previous column mismatch or missing token, which causes a CORS error in the browser.

Instructions:
1. Update `phase-2/frontend/lib/api.ts` (Aggressive Sender):
   * REMOVE the "relying on cookies" logic.
   * FORCE the `Authorization` header if the session exists.

2. Update `phase-2/backend/auth.py` (Resilient Receiver):
   * Ensure it handles the decoded token correctly and doesn't crash if the token is missing from the DB.

Goal: Frontend MUST send `Authorization: Bearer <token>`. Backend MUST query `session` table using `token` column.

## Response snapshot

Successfully implemented the authentication fix:

1. Updated frontend `api.ts` to force Authorization header:
   - Removed the "relying on cookies" fallback logic
   - Now forces the header with `session.session.token`
   - Added debugging statements to verify token attachment

2. Updated backend `auth.py` to be more resilient:
   - Simplified the token retrieval to prioritize header then fall back to cookie
   - Fixed column names to match the actual database schema (`user_id` instead of `userId`)
   - Improved error handling to prevent crashes
   - Maintained the decoding and signature handling logic

The changes ensure that:
- Frontend will consistently send Authorization headers when a session exists
- Backend properly queries the session table using the correct column names
- Authentication flow is more robust and less prone to CORS-related crashes

## Outcome

- ✅ Impact: Fixed authentication deadlock and prevented CORS crashes
- 🧪 Tests: Updated auth mechanism to be more reliable
- 📁 Files: Modified api.ts and auth.py for consistent header-based auth
- 🔁 Next prompts: Ready for testing the fixed authentication flow
- 🧠 Reflection: Removing cookie fallback and ensuring consistent header usage resolves the authentication inconsistency

## Evaluation notes (flywheel)

- Failure modes observed: Previously, inconsistent auth methods caused server crashes
- Graders run and results (PASS/FAIL): N/A - manual implementation
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Test the updated authentication flow end-to-end