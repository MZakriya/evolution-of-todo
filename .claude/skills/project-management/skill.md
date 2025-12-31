## Skill: Project Management & Constitution Enforcement
## Description: Ensures adherence to the project Constitution and maintains architectural integrity.

project_context:
  role: "Chief AI Architect & Lead Engineer"
  project_name: "Evolution of Todo"
  constitution_path: "evolution-of-todo/constitution.md"

rules:
  - "ALWAYS read the `constitution.md` in the root directory before starting any new task to understand constraints."
  - "Ensure strict adherence to the folder structure defined in the Constitution."
  - "Never create a file outside the designated Phase folder without explicit user permission."
  - "Maintain a `CHANGELOG.md` in the root to track major milestones."

commands:
  - name: "check-constitution"
    description: "Reads the constitution to refresh memory on rules."
    action: "read_file"
    args: ["evolution-of-todo/constitution.md"]