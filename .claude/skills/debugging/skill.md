## Skill: Debugging & Root Cause Analysis
## Description: Systematic approach to identifying, isolating, and fixing software defects.

protocol:
  1. **Analyze Traceback**: Read the full error message and stack trace carefully.
  2. **Reproduce**: Create a minimal reproduction script or test case to confirm the issue.
  3. **Isolate**: Determine if the issue is logic-based, environment-based, or dependency-based.
  4. **Hypothesize & Fix**: Propose a specific fix. Avoid rewriting entire files if a surgical fix is possible.
  5. **Verify**: Run the reproduction script again to ensure the error is resolved.

guidelines:
  - "Do not blindly apply fixes without understanding the root cause."
  - "Use print statements or logging to trace execution flow if the error is silent."
  - "Check `uv.lock` if the issue seems related to missing dependencies."
  - "If a fix fails twice, STOP and re-evaluate the approach or ask the user for help."

commands:
  - name: "analyze-error"
    description: "Reads error logs and suggests potential causes."
    usage: "analyze-error [log_file_path]"