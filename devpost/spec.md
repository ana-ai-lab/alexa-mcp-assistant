# Scope.md - Alexa+ MCP Agentic Productivity Assistant

**Hackathon:** Build, Ship, Shape: Amazon Developer Hackathon 2026  
**Track Principal:** Track Alexa+ (Simulación de Cliente Web y Servidor MCP)  
**Mini-desafíos:** AWS Builder / Open Source  

---

## 1. Resumen Ejecutivo (Elevator Pitch)
**Alexa+ MCP Agentic Productivity Assistant** es un asistente conversacional agéntico impulsado por un servidor **MCP (Model Context Protocol)** en Python y la API de **Google Gemini**. Permite a profesionales y desarrolladores orquestar tareas, procesar contextos de trabajo complejos y generar planes de acción estructurados en tiempo real a través de una interfaz de simulación de Alexa+.

---

## 2. Declaración del Problema y Solución

* **El Problema:** Los profesionales pierden tiempo valioso cambiando manualmente de contexto entre tomar notas informales, priorizar tareas en backlogs y estructurar resúmenes ejecutivos al inicio o cierre de sus jornadas.
* **La Solución:** Un servidor MCP modular que expone herramientas agénticas especializadas para que un cliente simulado de Alexa+ pueda interpretar la intención del usuario, ejecutar las herramientas necesarias y entregar resultados listos para exportar en un solo clic.

---

## 3. Alcance del MVP (48 Horas)

El MVP para la entrega del hackathon se centra en 3 componentes fundamentales de función única:

### A. Servidor MCP (Python)
Implementación de un servidor MCP ligero que expone **3 herramientas agénticas (*tools*)**:
1. `organize_tasks(raw_text)`: Analiza texto en bruto y extrae tareas priorizadas con estimaciones.
2. `summarize_workspace_context(notes)`: Genera resúmenes ejecutivos breves enfocados en bloqueos y siguientes pasos.
3. `export_action_plan(format)`: Formatea el resultado final en Markdown/JSON estructurado para Jira, Notion o Markdown.

### B. Cliente de Simulación Alexa+ (Streamlit)
* Interfaz web conversacional interactiva que simula la voz/chat de Alexa+.
* Visualizador de ejecución agéntica que muestra en tiempo real qué herramienta MCP se está invocando y con qué parámetros.

### C. Motor de Razonamiento (Google Gemini API)
* Uso de `gemini-1.5-flash` / `gemini-3.8-flash` como orquestador de intenciones para decidir qué herramienta MCP invocar según la solicitud del usuario.

---

## 4. Fuera de Alcance (Out of Scope para el Hackathon)

Para garantizar la entrega a tiempo, los siguientes elementos quedan fuera del MVP:
* Conexión con hardware físico de dispositivos Echo/Alexa o SDKs nativos cerrados.
* Autenticación multiusuario o base de datos relacional persistente.
* Integraciones activas con APIs de terceros de pago (se usarán salidas estándar en Markdown/JSON).

---

## 5. Pila Tecnológica

* **Lenguaje:** Python 3.12
* **Protocolo Agéntico:** Model Context Protocol (MCP) SDK
* **Modelo de IA:** Google Gemini API
* **Interfaz de Usuario:** Streamlit
* **Gestión de Entorno:** `python-dotenv` para aislamiento de API Keys (`.env`)
* **Control de Versiones:** Git / GitHub (Repositorio Público con Licencia MIT)

---

## 6. Criterios de Éxito para el Vídeo Demo (1-3 min)

1. Mostrar la conversación en la interfaz de Alexa+ ingresando notas informales de trabajo.
2. Demostrar la invocación automática de al menos 2 herramientas MCP por parte del agente.
3. Exportar el plan de acción en un solo clic.
4. Mostrar la estructura del repositorio en GitHub con la carpeta `devpost/` y los archivos `scope.md`, `prd.md` y `spec.md`.
2️⃣ devpost/prd.md
# Product Requirements Document (PRD)

## 📌 Visión General del Producto
**Nombre del Proyecto:** Alexa+ MCP Agentic Productivity Assistant  
**Categoría Hackathon:** Track Alexa+ / MCP & Agent Skills  
**Hackathon:** Build, Ship, Shape: Amazon Developer Hackathon 2026  

**Descripción:**  
Un asistente agéntico inteligente de productividad diseñado para integrarse con el ecosistema **Alexa+** mediante el protocolo **Model Context Protocol (MCP)**. La solución permite a profesionales y equipos organizar tareas, sintetizar contexto de trabajo y exportar planes de acción ejecutables mediante comandos en lenguaje natural.

---

## 🎯 Objetivos y Problema a Resolver
* **Problema:** La fragmentación de información y tareas diarias genera pérdida de tiempo y contexto en profesionales que gestionan múltiples proyectos.
* **Solución:** Un servidor MCP en Python que expone herramientas agénticas (*tools*) orquestadas por **Google Gemini**, ofreciendo un asistente de voz/texto simulado en una interfaz Streamlit.
* **Objetivo del MVP:** Demostrar en un vídeo de 1-3 minutos la invocación fluida de herramientas MCP para la organización y síntesis de productividad en tiempo real.

---

## 👥 Usuarios Objetivo (*User Personas*)
* **Product Owners y Desarrolladores:** Que necesitan sintetizar rápidamente pendientes y exportar acuerdos.
* **Usuarios del Ecosistema Alexa+:** Que buscan asistentes de voz/texto capaces de interactuar directamente con sus herramientas de trabajo locales a través del protocolo abierto MCP.

---

## 🚀 Requisitos Funcionales (Core Features)

### F1: Servidor MCP (*Model Context Protocol*) en Python
* **Invocación de Herramientas:** Implementación del protocolo MCP expuesto a través de herramientas (*tools*) estructuradas:
  1. `organize_tasks`: Categoriza y prioriza listas de tareas según impacto y urgencia.
  2. `summarize_workspace_context`: Extrae y sintetiza puntos clave de documentos o notas de trabajo.
  3. `export_action_plan`: Genera un plan de acción estructurado en Markdown listo para compartir.

### F2: Interfaz Cliente de Simulación Alexa+ (Streamlit)
* **Consola de Chat Conversacional:** Entrada de texto/voz simulada para interactuar con el asistente Alexa+.
* **Panel de Visualización de Herramientas MCP:** Muestra en tiempo real qué herramienta MCP ha sido seleccionada e invocada por el modelo, junto con los argumentos enviados y la respuesta.

### F3: Orquestador Agéntico (Google Gemini API)
* **Razonamiento y Selección de Tools:** Uso de la API de Gemini con *function calling* para decidir automáticamente qué herramientas del servidor MCP deben ejecutarse según la intención del usuario.

### F4: Exportación y Salida Estructurada
* **Formato Limpio:** Renderizado de la respuesta final en formato Markdown con botón para copiar el plan de acción al portapapeles.

---

## 🖥️ Flujo de Usuario (*User Flow*)
1. **Entrada:** El usuario ingresa una petición en lenguaje natural (ej. *"Sintetiza mis notas del proyecto y organízame un plan de acción para hoy"*).
2. **Orquestación:** Gemini analiza la intención y selecciona secuencialmente las herramientas MCP `summarize_workspace_context` y `organize_tasks`.
3. **Ejecución MCP:** El servidor MCP procesa los datos y devuelve la información estructurada al cliente Streamlit.
4. **Salida:** Streamlit presenta la respuesta conversacional de Alexa+, los *logs* visuales de las herramientas usadas y el plan de acción final descargable o copiable.

---

## 🔒 Requisitos No Funcionales (NFRs)
* **Rendimiento:** Respuesta completa en menos de 3 segundos por interacción.
* **Seguridad:** Aislamiento estricto de claves API mediante archivo `.env` ignorado en Git (`.gitignore`).
* **Portabilidad:** Proyecto ligero ejecutable en entorno virtual de Python (`.venv`) sin dependencias de hardware externo.

---

## 📈 Criterios de Éxito del MVP
* [x] Documento de alcance (`scope.md`) y PRD (`prd.md`) definidos.
* [x] Servidor MCP funcional con al menos 2 herramientas operativas.
* [x] Cliente Streamlit ejecutando consultas y mostrando el uso de MCP.
* [x] Repositorio público en GitHub con licencia abierta (MIT).
* [ ] Vídeo demostrativo de 1 a 3 minutos listo para subir a YouTube.
3️⃣ devpost/spec.md
# Technical Specification (SPEC.md)
## Alexa+ MCP Agentic Productivity Assistant

---

## 1. System Architecture & Flow

The system follows a lightweight, decoupled **Model Context Protocol (MCP)** architecture consisting of three core layers:

[ Gemini Flash Orchestrator ] ◄── ► [ Avisos del sistema y declaraciones de herramientas ]│▼ (Invocaciones de llamadas a herramientas MCP)[ Servidor MCP Python personalizado ]├── organizar_tareas(raw_notes)├── resumir_workspace_context(archivos)└── export_action_plan(tareas, formato)│▼ (Salida estructurada/Ejecución de Markdown)[ Respuesta de UI Streamlit e inspector de eventos MCP en tiempo real]

---

## 2. Directory Structure

alexa_mcp_assistant/├── .env # Claves API (git-ignored)├── .gitignore # Ignora .env, .venv, pycache├── README.md # Instrucciones de configuración y ejecución├── requisitos.txt # Dependencias del proyecto├── app.py # Interfaz de usuario principal Streamlit y controlador de cliente├── mcp_server/│ ├── init.py├── alcance.md # Documento de alcance y límites├── prd.md # Documento de requisitos del producto└── spec.md # Documento de especificaciones técnicas

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
 API de Google Gemini (gemini-3.8-flash / gemini-1.5-flash)
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
Prueba unitaria (herramientas MCP): Ejecute python -m mcp_server.tools para verificar el formato de salida de la herramienta.
Prueba de integración (llamada a función Gemini): Verificar la ejecución de la herramienta a través de app.py.
Verificación de UI y Live Inspector: Confirme que la barra lateral de Streamlit muestra llamadas de herramientas en tiempo real y parámetros JSON.
Comprobación de exportación: Verifique la funcionalidad de copia con un solo clic del plan de acción de Markdown generado.
