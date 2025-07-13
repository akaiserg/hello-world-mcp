from mcp import ClientSession, StdioServerParameters,types  
from mcp.client.stdio import stdio_client
import asyncio
import traceback


server_parameters = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"],
)



async def run():
    try:
        print("Starting stdio client")
        async with stdio_client(server_parameters) as (read, write):
            print("Client Connected, created a session")
            async with ClientSession(read, write) as session:
                print("Session initialized")
                await session.initialize()
                print("List of tools:")
                tools = await session.list_tools()
                print("list of tools: ", tools)
                print("calling get_weather tool")
                result = await session.call_tool("get_weather",arguments={"location": "Tokyo"})
                print("result: ", result)                                
    except Exception as e:
        print(traceback.format_exc())
        print(e)


if __name__ == "__main__":
    asyncio.run(run())