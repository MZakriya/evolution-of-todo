---
id: 1
title: "MCP Master Configuration"
stage: general
date: "2025-12-31"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "unknown"
command: "/sp.implement"
labels: ["mcp", "configuration", "postgres", "kubernetes", "memory", "puppeteer"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "mcp-master-config.md"
tests:
  - "none"
---

# MCP Master Configuration

## Prompt Text
```
@skills/spec-driven-dev

**Action: Generate All-in-One MCP Configuration**

The user wants to configure ALL necessary MCP servers for the entire project lifecycle immediately.

**Task:**
Create a file named `mcp-master-config.md` in the root directory.
This file must contain the **JSON Configuration Block** for `claude_desktop_config.json` including:

1.  **Postgres** (via `uvx mcp-server-postgres`)
    -   Arg: `postgresql://user:pass@localhost:5432/db` (Placeholder)
2.  **Kubernetes** (via `uvx mcp-server-kubernetes`)
    -   (Requires `kubectl` to be installed later, but set it up now).
3.  **Memory** (via `uvx mcp-server-memory`)
    -   To enable persistent memory for the agent.
4.  **Puppeteer** (via `uvx mcp-server-puppeteer`)
    -   For browser automation and testing.

**Format:**
Provide the raw JSON structure that the user can copy-paste.
Add a checklist of "Prerequisites" for each server (e.g., "Need valid DB URL", "Need kubectl installed").
```

## Response Text
Successfully created the MCP Master Configuration file with JSON configuration blocks for all required MCP servers (Postgres, Kubernetes, Memory, Puppeteer) and comprehensive prerequisites checklists for each server type.

## Outcome Impact
Created a comprehensive configuration file that enables setup of all necessary MCP servers for the project lifecycle with proper prerequisites documentation.

## Tests Summary
- none

## Files Summary
- Created mcp-master-config.md with JSON configuration for all MCP servers
- Added prerequisites checklist for each server type

## Next Prompts
- "/sp.implement" to continue with project implementation tasks
- Configure individual MCP servers based on the generated configuration

## Reflection Note
The configuration file provides a complete setup for all required MCP servers with proper documentation of prerequisites for each.

## Failure Modes Observed
- None - all tasks completed successfully

## Next Experiment to Improve Prompt Quality
Consider adding more specific configuration examples for different deployment scenarios.