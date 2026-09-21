"""Plantillas de prompting parametrizables (few-shot y chain-of-thought).

`main.py` no arma prompts a mano: llama a una de estas funciones con la
consulta del usuario y obtiene el prompt final ya armado con la técnica
correspondiente. Reemplazá los ejemplos por los de tu propio caso de uso
(consigna 1) antes de entregar.
"""

# --- Ejemplos few-shot de referencia (reemplazar por los del caso de uso propio) ---
EJEMPLOS_FEW_SHOT = [
    {
        "consulta": "Perdí mi tarjeta de débito, ¿qué tengo que hacer?",
        "respuesta": (
            "Por seguridad, bloqueá la tarjeta lo antes posible desde el home banking, "
            "la aplicación móvil o el canal telefónico oficial del banco. "
            "Luego solicitá la reposición por uno de los canales habilitados. "
            "No compartas claves, PIN ni códigos de seguridad."
        ),
    },
    {
        "consulta": "¿Qué necesito para solicitar una tarjeta de crédito?",
        "respuesta": (
            "Los requisitos pueden variar según la entidad y el producto. "
            "Generalmente se solicita identificación, verificación de ingresos y una evaluación crediticia. "
            "Para conocer las condiciones exactas, consultá los canales oficiales del banco."
        ),
    },
    {
        "consulta": "¿Cómo puedo hacer una transferencia desde home banking?",
        "respuesta": (
            "Ingresá al home banking o a la aplicación oficial del banco, accedé a la sección de transferencias, "
            "seleccioná la cuenta de origen e ingresá los datos del destinatario y el importe. "
            "Antes de confirmar, verificá cuidadosamente los datos. "
            "Nunca compartas contraseñas, token ni códigos de validación."
        ),
    },
    {
        "consulta": "Quiero saber cuánto dinero tengo en mi cuenta.",
        "respuesta": (
            "No puedo acceder a información personal ni consultar saldos de cuentas. "
            "Para verificar tu saldo, ingresá al home banking o a la aplicación oficial del banco. "
            "Si no podés acceder, comunicate con un canal oficial de atención."
        ),
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
