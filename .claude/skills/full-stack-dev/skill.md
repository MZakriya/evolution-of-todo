## Skill: Full Stack Web Development
## Description: Standards for building FastAPI backends and Next.js frontends.

backend_standards:
  framework: "FastAPI"
  structure:
    - "Use Routers (APIRouter) to modularize endpoints."
    - "Use Pydantic models for data validation (Schemas)."
    - "Implement Dependency Injection for services."
    - "Follow RESTful API naming conventions."

frontend_standards:
  framework: "Next.js (App Router)"
  styling: "Tailwind CSS"
  state_management: "React Hooks / Context API"
  api_integration: "Use typed fetch functions or Axios."

integration_rules:
  - "Ensure CORS is strictly configured in FastAPI."
  - "Frontend types must mirror Backend Pydantic models."
  - "Always handle API errors gracefully in the UI."