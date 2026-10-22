import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

from mcp_server.server import MCPAgentServer
from mcp_server.tools import GEMINI_TOOL_DECLARATIONS, MCP_TOOLS_MAP

# Cargar variables de entorno
load_dotenv()

# Configuración de página en Streamlit
st.set_page_config(
    page_title="Alexa+ MCP Productivity Assistant",
    page_icon="🎙️",
    layout="wide"
)

# Inicializar servidor MCP y clave API
mcp_server = MCPAgentServer()
api_key = os.getenv("GEMINI_API_KEY")

# Título de la aplicación
st.title("🎙️ Alexa+ MCP Agentic Productivity Assistant")
st.caption("Amazon Developer Hackathon Entry • Powered by Model Context Protocol (MCP) & Google Gemini API")

# Sidebar: Configuración e Inspector de Eventos MCP
with st.sidebar:
    st.header("⚙️ Servidor MCP Status")
    if api_key:
        st.success("✅ API Key configurada", icon="🔑")
    else:
        st.error("❌ GEMINI_API_KEY no encontrada en .env")

    st.subheader("🛠️ Herramientas MCP Registradas")
    for tool in mcp_server.list_tools():
        st.markdown(f"**`{tool['name']}`**\n_{tool['description']}_")

    st.divider()
    st.subheader("🔍 Inspector de Eventos MCP en Vivo")
    mcp_events_container = st.container()

# Historial de conversación y eventos
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mcp_events" not in st.session_state:
    st.session_state.mcp_events = []

# Mostrar historial en la barra lateral
with mcp_events_container:
    if st.session_state.mcp_events:
        for idx, event in enumerate(reversed(st.session_state.mcp_events), 1):
            with st.expander(f"Evento MCP #{len(st.session_state.mcp_events) - idx + 1}: {event['tool']}"):
                st.json(event)
    else:
        st.info("Sin eventos MCP ejecutados aún.")

# Renderizar chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de usuario
if prompt := st.chat_input("¿En qué puedo ayudarte hoy con tus tareas o reuniones?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if not api_key:
        st.error("Por favor agrega tu GEMINI_API_KEY al archivo .env para continuar.")
        st.stop()

    try:
        client = genai.Client(api_key=api_key)
        
        # System instruction y herramientas
        system_instruction = (
            "Eres Alexa+, un asistente agéntico de productividad conectado a un servidor MCP (Model Context Protocol). "
            "Tu objetivo es ayudar a transformar notas y pensamientos en planes de acción organizados. "
            "Usa siempre las herramientas MCP declaradas cuando la consulta lo requiera y responde con profesionalismo y claridad."
        )

        with st.chat_message("assistant"):
            with st.spinner("Alexa+ procesando la consulta con el servidor MCP..."):
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        tools=[types.Tool(function_declarations=GEMINI_TOOL_DECLARATIONS)]
                    )
                )

                # Verificar si Gemini solicita ejecutar una función MCP
                if response.function_calls:
                    for call in response.function_calls:
                        tool_name = call.name
                        args = call.args
                        
                        # Ejecutar la herramienta en el servidor MCP
                        execution_result = mcp_server.execute_tool(tool_name, args)
                        
                        # Registrar evento MCP para la demo
                        st.session_state.mcp_events.append({
                            "tool": tool_name,
                            "arguments": args,
                            "output": execution_result
                        })
                        
                        # Sintetizar la respuesta final con el resultado
                        synthesis_prompt = (
                            f"El usuario preguntó: '{prompt}'.\n"
                            f"Se ejecutó la herramienta MCP '{tool_name}' obteniendo este resultado:\n"
                            f"{json.dumps(execution_result, ensure_ascii=False)}\n\n"
                            f"Presenta una respuesta clara, bien formateada y amable como Alexa+."
                        )
                        
                        final_response = client.models.generate_content(
                            model="gemini-3.5-flash",
                            contents=synthesis_prompt
                        )
                        output_text = final_response.text
                else:
                    output_text = response.text

                st.markdown(output_text)
                st.session_state.messages.append({"role": "assistant", "content": output_text})
                st.rerun()

    except Exception as e:
        st.error(f"Error al comunicar con la API de Gemini o el servidor MCP: {str(e)}")
        