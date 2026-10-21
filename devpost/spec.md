# Technical Specification (SPEC.md)

## Alexa+ MCP Agentic Productivity Assistant

---

## 1. System Architecture & Flow

The system follows a lightweight, decoupled **Model Context Protocol (MCP)** architecture consisting of three core layers:

[ Usuario / UI Streamlit ]│▼ (Simulación de transcripción de audio / Mensaje)[ Gemini Flash Orchestrator ] ◄── ► [ Mensaje del sistema y declaraciones de herramientas ]│▼ (Llamada de herramienta MCP Invocaciones)[ Servidor MCP Python personalizado ]├── organizar_tasks(raw_notes)├── resume_workspace_context(files)└── export_action_plan(tareas, formato)│▼ (Salida estructurada/Ejecución de rebajas)[Respuesta de interfaz de usuario optimizada e inspector de eventos MCP en tiempo real]

---

## 2. Directory Structure

alexa_mcp_assistant/├── .env # Claves API (git-ignored)├── .gitignore # Ignora .env, .venv, pycache├── README.md # Instrucciones de configuración y ejecución├── requisitos.txt # Dependencias del proyecto├── app.py # Interfaz de usuario principal Streamlit y controlador de cliente├── mcp_server/│ ├── init.py│ ├── server.py # Controlador de servidor MCP personalizado│ └── tools.py # Implementación de las 3 herramientas MCP└── devpost/ # Paquete de documentación del Hackathon├── alcance.md # Documento de alcance y límites├── prd.md # Documento de requisitos del producto└── spec.md # Documento de especificaciones técnicas

---

## 3. MCP Tool Contracts & Schemas

### Tool 1: `organize_tasks`
* **Description:** Parses unstructured notes or conversational bullet points into a structured backlog of tasks with priorities and deadlines.
* **Input Schema:**
```json
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
Descripción: Analiza las entradas recientes del espacio de trabajo para producir un informe ejecutivo conciso y resaltar posibles cuellos de botella.
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
Descripción: Formatea las tareas y el resumen en un plan de acción de Markdown limpio y listo para copiar.
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
Modelo: API de Google Gemini (gemini-3.8-flash / gemini-1.5-flash)
Aviso del sistema:
Eres Alexa+, un asistente de productividad agente integrado con un servidor Model Context Protocol (MCP).Tu objetivo es ayudar a los usuarios a transformar pensamientos sin procesar, notas de reuniones y tareas en planes de acción estructurados.Inspecciona siempre las herramientas MCP disponibles y ejecuta llamadas de función cuando sea apropiado.Mantén un tono claro, conciso y profesional.
Bucle de llamada de función:
El usuario ingresa el mensaje en la interfaz de usuario de Streamlit.
Gemini procesa consultas con esquemas de herramientas declarados.
Si Gemini emite function_call, app.py pasa parámetros a mcp_server/tools.py.
La salida de la herramienta se devuelve a Gemini para la síntesis de la respuesta final.
La interfaz de usuario muestra la respuesta final y actualiza el panel de la barra lateral "MCP Event Inspector".
5. Seguridad y credenciales
Todos los secretos se almacenan estrictamente en .env: GEMINI_API_KEY=your_google_gemini_api_key_here
.gitignore previene fugas: .env, .venv/, __pycache__/, *.pyc
6. Dependencias técnicas (requirements.txt)
google-genai>=0.1.0
streamlit>=1.35.0
python-dotenv>=1.0.1
mcp>=1.0.0
7. Plan de verificación y pruebas
Prueba unitaria (herramientas MCP): Ejecute python -m mcp_server.tools para verificar el formato de salida de la herramienta.
Prueba de integración (llamada a función Gemini): Verificar la ejecución de la herramienta a través de app.py.
Verificación de UI y Live Inspector: Confirme que la barra lateral de Streamlit muestra llamadas de herramientas en tiempo real y parámetros JSON.
Comprobación de exportación: Verifique la funcionalidad de copia con un solo clic del plan de acción de Markdown generado.


