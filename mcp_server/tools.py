import json
import re
from typing import Dict, Any, List

def organize_tasks(raw_notes: str) -> Dict[str, Any]:
    """Procesa notas desordenadas en un backlog con prioridades y pasos de acción."""
    lines = [line.strip("- *•\t") for line in raw_notes.strip().split("\n") if line.strip()]
    tasks = []
    
    for idx, line in enumerate(lines, start=1):
        line_lower = line.lower()
        if any(w in line_lower for w in ["urgente", "urgent", "asap", "hoy", "crítico"]):
            priority = "HIGH"
        elif any(w in line_lower for w in ["después", "later", "opcional"]):
            priority = "LOW"
        else:
            priority = "MEDIUM"
            
        tasks.append({
            "id": f"TASK-{idx:03d}",
            "title": line[:60],
            "priority": priority,
            "actionable_step": f"Ejecutar y dar seguimiento a: {line}"
        })
        
    return {
        "status": "SUCCESS",
        "tasks_count": len(tasks),
        "tasks": tasks
    }


def summarize_workspace_context(context_text: str) -> Dict[str, Any]:
    """Genera un resumen ejecutivo y extrae los puntos clave del texto proporcionado."""
    sentences = [s.strip() for s in re.split(r'[.!?]\s+', context_text.strip()) if s.strip()]
    summary = f"Resumen Ejecutivo: {sentences[0]}." if sentences else "Sin contenido suficiente para resumir."
    takeaways = sentences[:3]
    
    return {
        "status": "SUCCESS",
        "summary": summary,
        "key_takeaways": takeaways,
        "action_items_count": len(sentences)
    }


def export_action_plan(title: str, tasks_markdown: str, notes: str = "") -> Dict[str, Any]:
    """Formatea tareas y observaciones en un plan de acción limpio en Markdown listo para copiar."""
    formatted_md = f"# 📋 Plan de Acción: {title}\n\n## 🎯 Objetivos y Tareas Clave\n{tasks_markdown}\n\n"
    if notes:
        formatted_md += f"## 📝 Notas Adicionales\n{notes}\n\n"
    formatted_md += "---\n*Generado automáticamente por Alexa+ MCP Agentic Productivity Assistant*"
    
    return {
        "status": "SUCCESS",
        "title": title,
        "formatted_markdown": formatted_md
    }


# Mapa de funciones ejecutables
MCP_TOOLS_MAP = {
    "organize_tasks": organize_tasks,
    "summarize_workspace_context": summarize_workspace_context,
    "export_action_plan": export_action_plan
}

# Declaración de herramientas para Gemini API
GEMINI_TOOL_DECLARATIONS = [
    {
        "name": "organize_tasks",
        "description": "Organiza notas sin estructurar o viñetas en una lista de tareas priorizadas.",
        "parameters": {
            "type": "OBJECT",
            "properties": {
                "raw_notes": {
                    "type": "STRING",
                    "description": "Texto sin estructurar o notas proporcionadas por el usuario."
                }
            },
            "required": ["raw_notes"]
        }
    },
    {
        "name": "summarize_workspace_context",
        "description": "Analiza el contexto del área de trabajo para generar un resumen ejecutivo y puntos clave.",
        "parameters": {
            "type": "OBJECT",
            "properties": {
                "context_text": {
                    "type": "STRING",
                    "description": "Texto del contexto o resumen del área de trabajo a analizar."
                }
            },
            "required": ["context_text"]
        }
    },
    {
        "name": "export_action_plan",
        "description": "Formatea tareas y notas en un plan de acción limpio en Markdown listo para copiar.",
        "parameters": {
            "type": "OBJECT",
            "properties": {
                "title": {
                    "type": "STRING",
                    "description": "Título principal del plan de acción."
                },
                "tasks_markdown": {
                    "type": "STRING",
                    "description": "Contenido de las tareas o puntos de acción formateados."
                },
                "notes": {
                    "type": "STRING",
                    "description": "Notas u observaciones adicionales opcionales."
                }
            },
            "required": ["title", "tasks_markdown"]
        }
    }
]
