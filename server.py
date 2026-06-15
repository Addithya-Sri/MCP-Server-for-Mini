from mcp.server.fastmcp import FastMCP
import random

# "Learning Server" is the name shown to clients
mcp = FastMCP("Learning Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def roll_dice(sides: int = 6) -> int:
    """Roll a die with the given number of sides"""
    return random.randint(1, sides)

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Welcome to your first MCP server."

if __name__ == "__main__":
    mcp.run()