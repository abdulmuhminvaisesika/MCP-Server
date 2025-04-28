import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient

model = ChatOllama(model="mistral")  # ✅ using your local model

async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [r"C:\Users\abdul.muhmin\Al&ML\MCP\math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/sse",  # Make sure the URL is correct
                "transport": "sse",  # Corrected to sse
            }
        }
    ) as client:

        # Create the agent
        agent = create_react_agent(model, client.get_tools())

         # Invoke the agent with a math query
        math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        math_result = math_response['messages'][-1].content  # Get the last AI message content
        print(f"Math Response: {math_result}")

        # Invoke the agent with a weather query
        weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
        weather_result = weather_response['messages'][-1].content  # Get the last AI message content
        print(f"Weather Response: {weather_result}")

# Run the asyncio loop
asyncio.run(main())
