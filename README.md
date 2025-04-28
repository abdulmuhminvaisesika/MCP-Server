# MCP - Model Context Protocol


## Introduction
MCP is an open protocol that standardizes how applications provide context to LLMs. MCP provides a standardized way to connect AI models to different data sources and tools.
MCP helps you build agents and complex workflows on top of LLMs.

## General architecture

At its core, MCP follows a client-server architecture where a host application can connect to multiple servers:

* MCP Hosts: Programs like Claude Desktop, IDEs, or AI tools that want to access data through MCP
* MCP Clients: Protocol clients that maintain 1:1 connections with servers
* MCP Servers: Lightweight programs that each expose specific capabilities through the standardized Model Context Protocol
* Local Data Sources: Your computer’s files, databases, and services that MCP servers can securely access
* Remote Services: External systems available over the internet (e.g., through APIs) that MCP servers can connect to
  

### Core architecture
Understand how MCP connects clients, servers, and LLMs

MCP follows a client-server architecture where:

* Hosts are LLM applications (like Claude Desktop or IDEs) that initiate connections
* Clients maintain 1:1 connections with servers, inside the host application
* Servers provide context, tools, and prompts to clients


### Core components

* Protocol layer - The protocol layer handles message framing, request/response linking, and high-level communication patterns.

* Transport layer - The transport layer handles the actual communication between clients and servers.
 
    1. Stdio transport : Uses standard input/output for communication
    2. HTTP with SSE transport : Uses Server-Sent Events for server-to-client messages(HTTP POST for client-to-server messages)
* Message types - MCP has these main types of messages:

    1. Requests: expect a response from the other side
    2. Results: are successful responses to requests
    3. Errors : indicate that a request failed
    4. Notifications: are one-way messages that don’t expect a response


### Connection lifecycle

1. Initialization

    1. Client sends initialize request with protocol version and capabilities
    2. Server responds with its protocol version and capabilities
    3. Client sends initialized notification as acknowledgment
    4. Normal message exchange begins


2. Message exchange

    After initialization, the following patterns are supported:

* Request-Response: Client or server sends requests, the other responds
* Notifications: Either party sends one-way messages
3. 
3. Termination

    Either party can terminate the connection:

* Clean shutdown via close()
* Transport disconnection
* Error conditions


### Error handling

MCP defines these standard error codes:

```python 
enum ErrorCode {
  // Standard JSON-RPC error codes
  ParseError = -32700,
  InvalidRequest = -32600,
  MethodNotFound = -32601,
  InvalidParams = -32602,
  InternalError = -32603
}
```
SDKs and applications can define their own error codes above -32000.
Errors are propagated through:
* Error responses to requests
* Error events on transports
* Protocol-level error handlers

## Implementation example

* Implemented a local AI agent using Ollama, LangChain, and MCP that can solve math problems by calling custom tools.
* Tried running multiple MCP servers and tested a LangGraph agent that uses MCP tools within a LangGraph API server.
* Here is the repo link: https://github.com/abdulmuhminvaisesika/MCP-Server


