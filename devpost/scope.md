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
