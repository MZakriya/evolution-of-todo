## Skill: Testing & Quality Assurance
## Description: Strategies for Unit, Integration, and End-to-End testing to validate Specs.

testing_frameworks:
  - "Python: Use `pytest` for all backend and logic testing."
  - "Async: Use `pytest-asyncio` for testing FastAPI/SQLModel async functions."

guidelines:
  - "Test Driven Development (TDD) Mindset: Write (or plan) tests *before* or *with* the implementation."
  - "One Spec Feature = One Test File (or clear Test Suite)."
  - "Mock external services (like OpenAI API or Database) during Unit Tests to save costs and speed up execution."

commands:
  - name: "run-tests"
    description: "Executes the test suite."
    usage: "uv run pytest"