from mcp.server.fastmcp import FastMCP
from app import get_ghibli_films  # film listesini döndüren fonksiyon

# MCP server başlatılıyor
mcp = FastMCP("films-mcp")

@mcp.tool()
async def get_films() -> dict:
    """
    Get a list of Ghibli films.
    """
    films = get_ghibli_films()
    return {"films": films}

if __name__ == "__main__":
    mcp.run(transport="stdio")
