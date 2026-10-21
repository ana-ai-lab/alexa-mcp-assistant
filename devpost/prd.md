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
