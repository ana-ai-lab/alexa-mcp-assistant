import json
from mcp_server.tools import MCP_TOOLS_MAP, GEMINI_TOOL_DECLARATIONS

class MCPAgentServer:
    """Servidor MCP que gestiona y ejecuta las herramientas agénticas."""
    def __init__(self, name: str = "alexa-mcp-productivity-server"):
        self.name = name
        self.tools = MCP_TOOLS_MAP

    def list_tools(self):
        """Retorna la lista de herramientas disponibles con sus esquemas."""
        return [
            {
                "name": decl["name"],
                "description": decl["description"],
                "inputSchema": decl["parameters"]
            }
            for decl in GEMINI_TOOL_DECLARATIONS
        ]

    def execute_tool(self, tool_name: str, arguments: dict):
        """Ejecuta la herramienta solicitada por el orquestador."""
        if tool_name not in self.tools:
            return {"status": "ERROR", "error": f"Herramienta '{tool_name}' no encontrada."}
        try:
            result = self.tools[tool_name](**arguments)
            return {"status": "SUCCESS", "tool": tool_name, "result": result}
        except Exception as e:
            return {"status": "ERROR", "tool": tool_name, "error": str(e)}


if __name__ == "__main__":
    server = MCPAgentServer()
    print(f"[{server.name} v1.0.0] Servidor MCP activo con {len(server.tools)} herramientas:")
    for t in server.list_tools():
        print(f"  • {t['name']}: {t['description']}")
        