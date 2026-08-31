# CLAUDE.md — Contexto general del Seminario de Ciencia de Datos II

Este repositorio cubre el **seminario completo**: un único repositorio, con una carpeta
por unidad (`unidad1/`, `unidad2/`, `unidad3/`, `unidad4/`), cada una con su propio
componente práctico. Este archivo raíz define el contexto y las reglas **comunes a todas
las unidades**. Para el detalle específico de cada unidad (contexto académico,
requerimientos funcionales, estructura de carpetas, tareas a generar), ver el
`CLAUDE.md` correspondiente dentro de cada carpeta de unidad (ej. `unidad1/CLAUDE.md`).

---

## 1. Restricciones de diseño (no negociables)

- **Costo:** cero para el estudiante. Solo herramientas y niveles gratuitos (Groq API,
  Gemini API, GitHub Codespaces, Google Colab). No asumir ni requerir tarjeta de crédito,
  suscripciones pagas, ni créditos de API de pago.
- **Hardware:** el proyecto debe correr en un Codespace estándar (2 núcleos, sin GPU). El
  único caso que requiere GPU es la rama PEFT/LoRA, y en ese caso la GPU es la de Google
  Colab (gratuita), nunca la del estudiante.
- **Lenguaje:** Python (versión 3.11 o superior).
- **Entorno:** GitHub Codespaces como entorno principal de desarrollo. El repositorio debe
  incluir una configuración de *dev container* que levante el entorno ya listo (sin pasos
  manuales de instalación de Python).
- **Seguridad:** ninguna API key se sube jamás al repositorio. Uso obligatorio de `.env`
  + `.gitignore`. No hardcodear credenciales en ningún archivo de código.
- **Estilo de código:** simplicidad ante todo, pensado para que un estudiante que recién
  se inicia pueda leer y entender el código sin esfuerzo. Ver política de calidad de
  código detallada en la sección 1.1.

### 1.1 Política de calidad de código (obligatoria)

- **Funciones con responsabilidad única y cortas:** cada función hace una sola cosa; si
  una función supera ~20-25 líneas o mezcla más de una responsabilidad (ej. leer config +
  llamar a la API + formatear salida), dividirla.
- **Evitar god classes / god functions:** ninguna clase o módulo debe concentrar toda la
  lógica del proyecto. Cada proveedor (Groq, Gemini) vive en su propio archivo; `main.py`
  solo orquesta, no implementa detalles de cada API.
- **Evitar magic numbers / magic strings:** todo valor "mágico" (cantidad de consultas de
  ejemplo, nombre de modelo, temperatura, nombres de variables de entorno) va como
  constante nombrada al inicio del módulo correspondiente, nunca repetido ni hardcodeado
  inline.
- **Evitar deuda técnica evitable:** sin código comentado "por las dudas", sin TODOs sin
  resolver al momento de la entrega, sin duplicación de lógica entre `groq_provider.py` y
  `gemini_provider.py` (lo común va en `base_provider.py` o en una función compartida).
- **Patrones de diseño: solo Factory, y solo donde ya se necesita.** Se aprueba
  explícitamente un **Factory Method simple** (una función `get_provider(name: str)` que
  devuelve la instancia correcta según `MODEL_PROVIDER`) para la creación de proveedores.
  No introducir otros patrones de diseño (Strategy, Observer, Singleton, etc.) aunque
  técnicamente podrían aplicar: priorizar la solución más simple y directa por sobre la
  más "elegante", ya que el público destinatario del código son estudiantes, no un
  equipo de producción.
- **Simplicidad por sobre abstracción:** si una interfaz abstracta formal (`abc.ABC`)
  no aporta claridad real para este alcance tan acotado (dos proveedores nada más), usar
  en su lugar una clase base simple o incluso funciones sueltas con la misma firma,
  documentadas con un docstring que explique el contrato esperado. Priorizar que el
  estudiante pueda leer el archivo de punta a punta sin necesitar conocer conceptos de
  POO avanzados.
- **Manejo de errores explícito pero simple:** capturar y explicar errores esperables
  (API key ausente, proveedor no reconocido, error de red) con mensajes claros; no
  agregar manejo de excepciones genérico o excesivo que no aporte valor pedagógico.

## 2. Patrón de dev container por unidad (obligatorio, no reabrir)

Este repositorio es un **monorepo con una carpeta por unidad** (`unidad1/`, `unidad2/`,
`unidad3/`, `unidad4/`), y cada unidad puede necesitar un entorno distinto (por ejemplo,
Unidad 3 con Docker-in-Docker para MLOps, Unidad 4 con dependencias de RAG/agentes).
GitHub Codespaces **no detecta automáticamente** un `devcontainer.json` ubicado dentro de
una subcarpeta como `unidad2/.devcontainer/devcontainer.json`: solo escanea la raíz del
repositorio y el patrón de "múltiples configuraciones" `.devcontainer/<nombre>/devcontainer.json`.

Por eso, **toda config de Codespaces de cualquier unidad debe crearse en la raíz del
repositorio**, nunca dentro de la carpeta de la unidad:

```
.devcontainer/
├── unidad1/devcontainer.json
├── unidad2/devcontainer.json   (cuando exista)
├── unidad3/devcontainer.json   (cuando exista)
└── unidad4/devcontainer.json   (cuando exista)
```

Cada `devcontainer.json` debe fijar `"workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}/unidadN"`
para que el Codespace abra directamente en la carpeta de esa unidad (así el estudiante no
necesita hacer `cd` manualmente), y su `postCreateCommand` debe instalar únicamente el
`requirements.txt` de esa unidad. Cada unidad es así independiente y autocontenida: sumar
o modificar la config de una no afecta a las demás.

En el README de cada unidad, la instrucción para crear el Codespace debe indicar
explícitamente **Code → Codespaces → "..." (tres puntos) → New with options → elegir la
config de la unidad correspondiente**, no el atajo de un clic ("Create codespace on
main"), porque ese atajo no garantiza qué configuración usa cuando hay varias disponibles.
