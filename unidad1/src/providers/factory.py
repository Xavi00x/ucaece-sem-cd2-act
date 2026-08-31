"""Factory Method simple para instanciar el proveedor según MODEL_PROVIDER.

Único patrón de diseño aprobado en este proyecto (ver CLAUDE.md, sección 1.1).
`main.py` llama a `get_provider()` una sola vez y no necesita saber nada más
sobre cómo se construye cada proveedor.
"""

from src.providers.base_provider import BaseProvider
from src.providers.gemini_provider import GeminiProvider
from src.providers.groq_provider import GroqProvider

# --- Nombres válidos de MODEL_PROVIDER ---
PROVIDER_GROQ = "groq"
PROVIDER_GEMINI = "gemini"


def get_provider(name: str) -> BaseProvider:
    """Devuelve la instancia de proveedor correspondiente a `name`.

    `name` debe ser "groq" o "gemini" (valor de la variable de entorno
    MODEL_PROVIDER). Lanza ValueError si el nombre no es reconocido.
    """
    nombre_normalizado = name.strip().lower()

    if nombre_normalizado == PROVIDER_GROQ:
        return GroqProvider()

    if nombre_normalizado == PROVIDER_GEMINI:
        return GeminiProvider()

    raise ValueError(
        f"Proveedor '{name}' no soportado. Usá '{PROVIDER_GROQ}' o '{PROVIDER_GEMINI}' "
        "en la variable de entorno MODEL_PROVIDER."
    )
