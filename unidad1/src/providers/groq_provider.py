"""Proveedor de inferencia para modelos de pesos abiertos servidos por Groq."""

import os

from groq import Groq

from src.providers.base_provider import BaseProvider

# --- Constantes del proveedor (nada de "magic strings/numbers" inline) ---
GROQ_API_KEY_ENV_VAR = "GROQ_API_KEY"
GROQ_MODEL_NAME = "llama-3.1-8b-instant"
GROQ_TEMPERATURE = 0.7


class GroqProvider(BaseProvider):
    """Genera respuestas usando un modelo de pesos abiertos vía la API de Groq."""

    def __init__(self):
        api_key = os.environ.get(GROQ_API_KEY_ENV_VAR)
        if not api_key:
            raise ValueError(
                f"Falta la variable de entorno {GROQ_API_KEY_ENV_VAR}. "
                "Obtené una key gratuita en console.groq.com y agregala a tu archivo .env."
            )
        self._client = Groq(api_key=api_key)

    def generate(self, prompt: str) -> str:
        try:
            respuesta = self._client.chat.completions.create(
                model=GROQ_MODEL_NAME,
                temperature=GROQ_TEMPERATURE,
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as error:
            raise RuntimeError(
                f"Error al consultar la API de Groq: {error}"
            ) from error

        return respuesta.choices[0].message.content
