## Skill: MCP Server Development
## Description: Building custom Model Context Protocol (MCP) servers to expose data and tools to AI Agents.

core_components:
  - **Resources**: Data that the LLM can read (like a file or database row).
  - **Prompts**: Pre-defined templates to help the LLM use the server.
  - **Tools**: Executable functions (e.g., `add_task`, `delete_task`) that the LLM can call.

implementation_standards:
  - "Use the official `mcp` Python SDK."
  - "Define the server using `FastMCP` or standard Server class."
  - "Ensure all Tools have clear docstrings and type hints (JSON Schema generation depends on this)."
  - "Handle errors gracefully within tools so the Agent knows what went wrong without crashing."

code_structure:
  - "Keep MCP logic separate from core business logic."
  - "Use decorators like `@mcp.tool()` to register functions."

testing:
  - "Test MCP servers using the `mcp-inspector` or by connecting a local Claude Desktop instance."