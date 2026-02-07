# Skill: Model Context Protocol (MCP)

## Purpose

Standardizes how the Agent interacts with local tools (Filesystem, Git) and remote resources.

## Configuration Strategy

1. **Discovery**: Check `mcp_server_config.json` for active servers.
2. **Tool Use**: Prefer MCP Tools over ad-hoc shell scripts.
3. **Resources**: Use `mcp://` URI scheme for context attachment.

## Recommended Servers

* `@modelcontextprotocol/server-filesystem`: For controlled file access.
* `@modelcontextprotocol/server-github`: For issue tracking.
* `@modelcontextprotocol/server-postgres`: For direct DB schema introspection.
