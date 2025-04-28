from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers """

    return a + b

@mcp.tool()
def mutltiply(a: int, b: int) -> int:
    """Multiply twonumbers"""

    return a * b


if __name__ == "__main__":
    mcp.run(transport = "stdio")