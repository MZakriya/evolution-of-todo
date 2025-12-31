## Skill: Security Best Practices (SecOps)
## Description: Ensuring code security, secret management, and safe data handling.

secret_management:
  - "NEVER hardcode secrets (API keys, passwords, tokens) in source code."
  - "Always use Environment Variables loaded from a `.env` file."
  - "Ensure `.env` is added to `.gitignore` immediately upon creation."

input_validation:
  - "Validate all user inputs using Pydantic models."
  - "Sanitize inputs to prevent SQL Injection (handled by SQLModel, but be aware of raw queries)."
  - "Sanitize LLM outputs before displaying them to users (prevent XSS or prompt injection)."

review_checklist:
  - "Scan code for potential security vulnerabilities before finalizing implementation."