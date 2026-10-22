# Technical Specification (SPEC.md)

## Alexa+ MCP Agentic Productivity Assistant

---

## 1. System Architecture & Flow

The system follows a lightweight, decoupled **Model Context Protocol (MCP)** architecture consisting of three core layers:

- **User / Streamlit UI:** Handles user input and displays real-time responses.
- **Gemini Flash Orchestrator:** Manages system prompts and tool declarations.
- **Custom Python MCP Server:** Executes `organize_tasks`, `summarize_workspace_context`, and `export_action_plan`.

---

## 2. Directory Structure

- `app.py`: Main Streamlit UI & Client Controller
- `mcp_server/`: Custom MCP Server Handler and Tools
  - `server.py`: Server logic
  - `tools.py`: Tool implementations
- `devpost/`: Hackathon Documentation (`scope.md`, `prd.md`, `spec.md`)
- `requirements.txt`: Project dependencies
- `.env`: API Key configuration (git-ignored)
- `.gitignore`: Git exclusion file

---

## 3. MCP Tool Contracts & Schemas

### Tool 1: organize_tasks
- **Description:** Parses unstructured notes into a structured backlog of tasks.
- **Input:** `raw_notes` (string, required)
- **Output:** Array of tasks with `id`, `title`, `priority`, `actionable_step`.

### Tool 2: summarize_workspace_context
- **Description:** Analyzes workspace inputs to produce a concise executive briefing.
- **Input:** `context_text` (string, required)
- **Output:** `summary`, `key_takeaways`, `action_items_count`.

### Tool 3: export_action_plan
- **Description:** Formats tasks and summary into a clean Markdown action plan.
- **Input:** `title` (string, required), `tasks_markdown` (string, required), `notes` (string, optional)
- **Output:** `formatted_markdown`, `status`.

---

## 4. Gemini API & Orchestration Logic

- **Model:** Google Gemini API (`gemini-3.5-flash` / `gemini-3.8-flash`)
- **System Prompt:** You are Alexa+, an agentic productivity assistant integrated with a Model Context Protocol (MCP) server. Your goal is to assist users in transforming raw thoughts, meeting notes, and tasks into structured action plans.
- **Workflow:**
  1. User enters prompt in Streamlit UI.
  2. Gemini processes query with declared tool schemas.
  3. If Gemini emits function_call, `app.py` passes parameters to `mcp_server/tools.py`.
  4. Tool output is fed back to Gemini for final response synthesis.
  5. UI displays final response and updates the MCP Event Inspector panel.

---

## 5. Security & Credentials

- Secrets are stored in `.env` (`GEMINI_API_KEY`).
- `.gitignore` prevents committing secrets to public repositories.

---

## 6. Technical Dependencies

- `google-genai>=0.1.0`
- `streamlit>=1.35.0`
- `python-dotenv>=1.0.1`
- `mcp>=1.0.0`

---

## 7. Verification & Testing Plan

1. **Unit Test (MCP Tools):** Verify tool output formatting.
2. **Integration Test:** Verify tool execution through `app.py`.
3. **UI Check:** Confirm Streamlit sidebar displays real-time tool calls and parameter JSON.
4. **Export Check:** Verify one-click copy functionality.
