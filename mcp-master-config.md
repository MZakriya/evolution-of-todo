# MCP Master Configuration

This file contains the JSON configuration block for `claude_desktop_config.json` including all necessary MCP servers for the project lifecycle.

## JSON Configuration Block

```json
{
  "mcp_servers": {
    "postgres": {
      "command": "uvx mcp-server-postgres",
      "args": ["postgresql://user:pass@localhost:5432/db"],
      "description": "PostgreSQL database server for the application"
    },
    "kubernetes": {
      "command": "uvx mcp-server-kubernetes",
      "args": [],
      "description": "Kubernetes server for container orchestration"
    },
    "memory": {
      "command": "uvx mcp-server-memory",
      "args": [],
      "description": "Memory server for persistent agent memory"
    },
    "puppeteer": {
      "command": "uvx mcp-server-puppeteer",
      "args": [],
      "description": "Puppeteer server for browser automation and testing"
    }
  }
}
```

## Prerequisites Checklist

### Postgres Server
- [ ] PostgreSQL must be installed and running on the system
- [ ] Valid database URL with appropriate credentials
- [ ] Database server accessible at localhost:5432 (or configured port)
- [ ] User account with necessary permissions to the target database

### Kubernetes Server
- [ ] `kubectl` must be installed and configured
- [ ] Kubernetes cluster accessible (local or remote)
- [ ] Proper authentication configured for the cluster
- [ ] `kubeconfig` file properly set up

### Memory Server
- [ ] Sufficient disk space for persistent memory storage
- [ ] Appropriate permissions to write/read memory files
- [ ] Configured storage path is accessible and persistent

### Puppeteer Server
- [ ] Chrome/Chromium browser installed on the system
- [ ] Proper permissions to launch browser processes
- [ ] Sufficient system resources for browser automation
- [ ] Dependencies for Puppeteer properly installed