import asyncio
from fastmcp import Client, FastMCP

# HTTP server
client = Client("https://scamwolf.it/mcp")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()
        
        # Execute operations
        result = await client.call_tool("classify_text_get_response", {"text": "US stock trading tools are free and open, you can make money even if you don't understand anything. Win $10000 now! Call me back!"})
        print(result)

asyncio.run(main())
