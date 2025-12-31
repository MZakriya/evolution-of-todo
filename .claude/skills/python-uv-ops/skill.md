## Skill: Python Development with UV
## Description: Manages Python environment, dependencies, and execution using UV.

tools:
  package_manager: "uv"
  python_version: "3.13+"

commands:
  - name: "init-project"
    description: "Initialize a new Python project with UV."
    command: "uv init"
  
  - name: "add-dependency"
    description: "Add a new package."
    usage: "uv add [package_name]"

  - name: "run-script"
    description: "Run a python script using UV."
    usage: "uv run [script_path]"

  - name: "sync-env"
    description: "Sync the environment with uv.lock."
    command: "uv sync"

guidelines:
  - "Always use `uv run` to execute scripts to ensure the correct virtual environment is used."
  - "Never use `pip install` directly; always use `uv add` to maintain the lockfile."