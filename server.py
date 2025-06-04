from mcp.server.fastmcp import FastMCP
from app import get_ghibli_films  # Yukarıdaki fonksiyon burada çağrılıyor

mcp = FastMCP("films-mcp")

@mcp.tool()
async def get_films(name: str) -> dict:
    films = get_ghibli_films()

    if isinstance(films, dict) and "error" in films:
        return films

    if name:
        result = [f for f in films if name.lower() in f["title"].lower()]
        return {"films": result or f"'{name}' adlı film bulunamadı."}

    return {"films": films}

if __name__ == "__main__":
    mcp.run(transport="stdio")
