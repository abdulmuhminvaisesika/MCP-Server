# graph.py
from contextlib import asynccontextmanager
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic

# Define the model you want to use
model = ChatAnthropic(model="claude-3-5-sonnet-latest")

# Define the async context manager for the graph setup
@asynccontextmanager
async def make_graph():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [r"C:\Users\abdul.muhmin\Al&ML\MCP\math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/sse",  # Ensure the weather server is running
                "transport": "sse",
            }
        }
    ) as client:
        # Create the LangGraph agent using the tools from MCP client
        agent = create_react_agent(model, client.get_tools())
        yield agent  # Yield the agent for use in the LangGraph API server

