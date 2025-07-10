import asyncio
import json

from fastmcp import Client

"""
Analyze scams by ScamWolf, the advanced scam analyzer using MCP.

Author: ScamWolf

Access more ScamWolf products (web interface, REST API, Messenger bots...) at https://scamwolf.com
"""

# HTTP server
client = Client("https://scamwolf.it/mcp")


async def main():
    async with client:
        print("#########################")
        print("## ScamWolf MCP Client ##")
        print("#########################\n\n")

        # Test the connection
        if not await client.ping():
            print("Connection failed, please try again later.")
            return

        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        print("# ScamWolf Tools:\n")
        for tool in tools:
            print(tool.name)

        for resource in resources:
            print("\n# ScamWolf Resources:\n")
            print(resource)

        for prompt in prompts:
            print("\n# ScamWolf Prompts:\n")
            print(prompt.name)

        # Analyze a text for scams
        print("\n# ScamWolf MCP usage example:\n")
        result = await client.call_tool(
            "classify_text_get_response",
            {
                "text": "US stock trading tools are free and open, you can make money even if you don't understand anything. Win $10000 now! Call me back!"
            },
        )
        result_json = json.loads(result.content[0].text)

        print(
            f"Verdict for request {result_json['identifier']} - {result_json['status']}"
        )
        if result_json["status"] == "AVAILABLE":
            print(f"Money detected: ${result_json['classification']['money_total']}")
            if result_json["classification"]["is_investment_scam"]:
                print("Investment scam detected!")


asyncio.run(main())
