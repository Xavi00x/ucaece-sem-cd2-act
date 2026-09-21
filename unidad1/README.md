# Asistente virtual de atención bancaria con Gemini

Proyecto desarrollado como implementación de un asistente virtual de atención al cliente para una entidad bancaria utilizando un Foundation Model.

## Caso de uso

La solución busca responder consultas bancarias generales de forma automática, rápida y consistente.

El asistente puede atender preguntas relacionadas con:

- productos y servicios bancarios;
- tarjetas de débito y crédito;
- transferencias;
- home banking;
- préstamos;
- procedimientos generales de atención.

La solución está diseñada para no acceder ni responder consultas que requieran información personal del cliente, como saldos, movimientos o datos particulares de una cuenta.

Cuando una consulta requiere información privada o una gestión específica, el asistente indica al usuario que debe utilizar los canales oficiales o comunicarse con un operador.

## Modelo utilizado

Se utiliza **Gemini** mediante API.

La aplicación no ejecuta el modelo localmente. El código Python construye el prompt, envía la solicitud a Gemini y procesa la respuesta recibida.

## Estrategia de adaptación

Se utiliza **few-shot prompting**.

El prompt incorpora ejemplos de consultas y respuestas bancarias antes de presentar la consulta real del usuario.

Los ejemplos permiten orientar al modelo respecto de:

- el tipo de respuesta esperada;
-- el tono utilizado;
- las recomendaciones de seguridad;
- el tratamiento de información sensible;
- las situaciones que deben derivarse a canales oficiales.

Los ejemplos utilizados se encuentran en:

`src/prompt_templates.py`

## Consultas de prueba

La implementación ejecuta tres consultas representativas:

1. Tarjeta bloqueada luego de ingresar incorrectamente el PIN.
2. Solicitud de un préstamo personal desde la aplicación bancaria.
3. Consulta sobre los últimos movimientos de una cuenta.

La tercera consulta permite verificar que el asistente no intente acceder o inventar información personal del cliente.

## Estructura principal

```text
unidad1/
├── .env.example
├── evidencias.md
├── requirements.txt
├── README.md
└── src/
    ├── main.py
    ├── prompt_templates.py
    └── providers/
        ├── base_provider.py
        ├── factory.py
        ├── gemini_provider.py
        └── groq_provider.py
```

## Configuración

Crear el archivo de variables de entorno:

```bash
cp .env.example .env
```

Configurar:

```env
MODEL_PROVIDER=gemini
GEMINI_API_KEY=TU_API_KEY
```

La API key no debe incorporarse al repositorio.

## Ejecución

Desde la carpeta `unidad1` ejecutar:

```bash
python -m src.main
```

El programa procesa las tres consultas configuradas y muestra las respuestas obtenidas en la terminal.

Además, genera automáticamente:

`evidencias.md`

Este archivo contiene para cada prueba:

- la consulta realizada;
- el prompt few-shot completo;
- la respuesta generada por Gemini.

## Resultado

La ejecución permite comprobar que Gemini puede adaptar sus respuestas al contexto de atención bancaria mediante few-shot prompting, sin necesidad de realizar fine-tuning ni utilizar hardware especializado.

También se verifica que el asistente puede distinguir consultas generales de aquellas que requieren información privada, derivando estas últimas hacia canales oficiales de atención.
