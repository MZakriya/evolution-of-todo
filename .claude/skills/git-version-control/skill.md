## Skill: Git & Version Control Standards
## Description: Managing code history and collaboration using Git best practices.

commit_standards:
  - "Format: `type(scope): description`"
  - "Types:"
    - `feat`: New feature (e.g., `feat(todo): add delete functionality`)
    - `fix`: Bug fix (e.g., `fix(db): resolve connection timeout`)
    - `docs`: Documentation only (e.g., `docs: update constitution`)
    - `refactor`: Code change that neither fixes a bug nor adds a feature
    - `chore`: Build process or auxiliary tool changes

workflow:
  - "Before committing, check `git status` to ensure no unwanted files (like .env or __pycache__) are staged."
  - "Write descriptive commit messages that explain *why* a change was made."
  - "Use `.gitignore` strictly."

commands:
  - name: "status-check"
    command: "git status"