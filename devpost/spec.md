# Technical Specification (SPEC.md)

## Alexa+ MCP Agentic Productivity Assistant

---

## 1. System Architecture & Flow

The system follows a lightweight, decoupled **Model Context Protocol (MCP)** architecture consisting of three core layers:

```text
[ User / Streamlit UI ]
        │
        ▼ (Prompt / Audio Transcript Simulation)
[ Gemini Flash Orchestrator ] ◄──► [ System Prompt & Tool Declarations ]
        │
        ▼ (MCP Tool Call Invocations)
[ Custom Python MCP Server ]
   ├── organize_tasks(raw_notes)
   ├── summarize_workspace_context(files)
   └── export_action_plan(tasks, format)
        │
        ▼ (Structured Output / Markdown Execution)
[ Streamlit UI Response & Real-Time MCP Event Inspector ]
2. Estructura del directorio
alexa_mcp_assistant/
├── .env                    # API Keys (git-ignored)
├── .gitignore              # Ignores .env, .venv, __pycache__
├── README.md               # Setup and execution instructions
├── requirements.txt        # Project dependencies
├── app.py                  # Main Streamlit UI & Client Controller
├── mcp_server/
│   ├── __init__.py
│   ├── server.py           # Custom MCP Server Handler
│   └── tools.py            # Implementation of the 3 MCP tools
└── devpost/                # Hackathon Documentation Package
    ├── scope.md            # Scope & Boundaries Document
    ├── prd.md              # Product Requirements Document
    └── spec.md             # Technical Specification Document
3. Contratos y esquemas de herramientas MCP
Herramienta 1: organize_tasks
Description:Analiza notas no estructuradas o viñetas de conversación en una acumulación estructurada de tareas con prioridades y fechas límite.
Esquema de entrada:
{
  "raw_notes": "string (Required) - Unstructured text from the user"
}
Esquema de salida:
{
  "tasks": [
    {
      "id": "TASK-001",
      "title": "string",
      "priority": "HIGH | MEDIUM | LOW",
      "actionable_step": "string"
    }
  ]
}
Herramienta 2: summarize_workspace_context
Description:Analiza las aportaciones recientes al espacio de trabajo para producir un informe ejecutivo conciso y resaltar posibles obstáculos.
Esquema de entrada:
{
  "context_text": "string (Required) - Workspace summary or recent user activity"
}
Esquema de salida:
{
  "summary": "string",
  "key_takeaways": ["string"],
  "action_items_count": "integer"
}
Herramienta 3: export_action_plan
Description:Formatea las tareas y el resumen en un plan de acción de Markdown limpio y listo para copiar.
Esquema de entrada:
{
  "title": "string (Required)",
  "tasks_markdown": "string (Required)",
  "notes": "string (Optional)"
}
Esquema de salida:
{
  "formatted_markdown": "string",
  "status": "SUCCESS"
}
4. API de Gemini y lógica de orquestación
 / gemini-1.5-flash)
Aviso del sistema:
You are Alexa+, an agentic productivity assistant integrated with a Model Context Protocol (MCP) server.
Your goal is to assist users in transforming raw thoughts, meeting notes, and tasks into structured action plans.
Always inspect available MCP tools and execute function calls when appropriate.
Maintain a clear, concise, and professional tone.
Bucle de llamada de función:
El usuario ingresa el mensaje en la interfaz de usuario de Streamlit.
Gemini procesa consultas con esquemas de herramientas declarados.
Si Gemini emite function_call, app.py pasa parámetros a mcp_server/tools.py.
La salida de la herramienta se devuelve a Gemini para la síntesis de la respuesta final.
La interfaz de usuario muestra la respuesta final y actualiza el panel de la barra lateral "MCP Event Inspector".
5. Seguridad y credenciales
Todos los secretos se almacenan estrictamente en .env:
GEMINI_API_KEY=your_google_gemini_api_key_here
.gitignore evita fugas:
.env
.venv/
__pycache__/
*.pyc
6. Dependencias técnicas (requirements.txt)
google-genai>=0.1.0
streamlit>=1.35.0
python-dotenv>=1.0.1
mcp>=1.0.0
7. Plan de verificación y pruebas
 Ejecute python -m mcp_server.tools para verificar el formato de salida de la herramienta.
Prueba de integración (llamada a función Gemini): Verificar la ejecución de la herramienta a través de app.py.
UI & Live Inspector Check:Confirme que la barra lateral de Streamlit muestre llamadas a herramientas en tiempo real y el parámetro JSON.
Comprobación de exportación: Verifique la funcionalidad de copia con un solo clic del plan de acción de Markdown generado.

