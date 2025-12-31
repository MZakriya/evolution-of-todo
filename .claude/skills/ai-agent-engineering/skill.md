## Skill: AI Agent & MCP Engineering
## Description: Building intelligent chatbots using OpenAI SDK and Model Context Protocol (MCP).

core_concepts:
  - "Agents must have a System Prompt defining their personality and constraints."
  - "Use 'Tools' (Function Calling) to allow Agents to interact with the Todo Database."
  - "Implement MCP Servers to expose internal APIs to external AI tools."

implementation_rules:
  - "Use OpenAI Agents SDK for orchestrating the conversation."
  - "Ensure tool outputs are sanitized before feeding back to the LLM."
  - "Maintain conversation history (Context Window management)."
  - "For MCP: Follow the official MCP SDK python implementation patterns."