"""Plantillas de prompting parametrizables (few-shot y chain-of-thought).

`main.py` no arma prompts a mano: llama a una de estas funciones con la
consulta del usuario y obtiene el prompt final ya armado con la técnica
correspondiente. Reemplazá los ejemplos por los de tu propio caso de uso
(consigna 1) antes de entregar.
"""

# --- Ejemplos few-shot de referencia (reemplazar por los del caso de uso propio) ---
EJEMPLOS_FEW_SHOT = [
    {
        "consulta": "¿Cómo restablezco mi contraseña?",
        "respuesta": "Andá a Configuración > Seguridad > Restablecer contraseña y seguí los pasos indicados.",
    },
    {
        "consulta": "¿Cuál es el horario de atención?",
        "respuesta": "Atendemos de lunes a viernes de 9 a 18 hs (hora Argentina).",
    },
]

INSTRUCCION_CHAIN_OF_THOUGHT = (
    "Antes de responder, pensá el problema paso a paso en voz alta. "
    "Al final, escribí la respuesta definitiva precedida por 'Respuesta:'."
)


def construir_prompt_few_shot(consulta: str, ejemplos: list[dict] = EJEMPLOS_FEW_SHOT) -> str:
    """Arma un prompt few-shot: muestra pares consulta/respuesta de ejemplo y
    al final agrega la consulta real del usuario sin responder."""
    bloques_ejemplo = [
        f"Consulta: {ejemplo['consulta']}\nRespuesta: {ejemplo['respuesta']}"
        for ejemplo in ejemplos
    ]
    ejemplos_formateados = "\n\n".join(bloques_ejemplo)

    return (
        f"{ejemplos_formateados}\n\n"
        f"Consulta: {consulta}\n"
        "Respuesta:"
    )


def construir_prompt_chain_of_thought(consulta: str) -> str:
    """Arma un prompt chain-of-thought: le pide al modelo razonar paso a paso
    antes de dar la respuesta final."""
    return f"{INSTRUCCION_CHAIN_OF_THOUGHT}\n\nConsulta: {consulta}"
