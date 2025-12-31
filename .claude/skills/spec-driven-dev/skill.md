## Skill: Spec-Driven Development Workflow
## Description: Manages the lifecycle of converting Markdown Specs into executable Code.

workflow_steps:
  1. **Read Spec**: Always start by reading the relevant specification file in the `specs/` folder.
  2. **Analyze**: Break down the spec into logical implementation steps.
  3. **Plan**: Propose a file structure and logic flow to the user.
  4. **Implement**: Generate code only after the plan is approved.
  5. **Verify**: Ensure the generated code matches the Spec requirements exactly.

constraints:
  - "NO MANUAL CODING: You must generate all code."
  - "Do not hallucinate features not present in the Spec."
  - "If a Spec is ambiguous, ASK the user for clarification before coding."
  - "Always check if a previous version of the code exists before overwriting."

commands:
  - name: "implement-feature"
    description: "Implements a feature based on a provided spec file path."
    usage: "implement-feature [path_to_spec_file]"