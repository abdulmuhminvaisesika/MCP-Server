from langgraph import LangGraphAPI
import asyncio

async def start_api():
    app = LangGraphAPI(graph_path="./graph.py")  # Make sure the path to your graph.py is correct
    await app.start()

asyncio.run(start_api())
