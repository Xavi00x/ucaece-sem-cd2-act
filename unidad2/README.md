# Unidad 2 - Auditoría de equidad en selección de personal

## Descripción

Este proyecto corresponde a la actividad formativa de la Unidad 2 de Seminario de Ciencia de Datos II, de la Licenciatura en Ciencia de Datos de la Universidad CAECE.

El trabajo analiza posibles sesgos de género en un modelo de clasificación de candidatos laborales, tomando como referencia el caso del sistema de reclutamiento automatizado de Amazon (2018).

## Dataset

Se utilizó **Predicting Hiring Decisions in Recruitment Data**, disponible en Kaggle:

https://www.kaggle.com/datasets/rabieelkharoua/predicting-hiring-decisions-in-recruitment-data

El dataset contiene 1.500 registros de candidatos y 11 columnas.

- Variable objetivo: `HiringDecision` (0 = no contratado, 1 = contratado).
- Atributo sensible: `Gender` (0 = hombre, 1 = mujer).
- Modelo utilizado: regresión logística.

Se utilizan para estudiar un problema comparable de equidad en la selección de personal.

## Auditoría de equidad

Se utilizó Fairlearn para calcular dos métricas:

- Demographic parity difference.
- Equalized odds difference.

### Resultados

| Escenario | Exactitud | Demographic parity diff. | Equalized odds diff. |
|---|---|---|---|
| Modelo base | 0.873 | 0.033 | 0.032 |
| ExponentiatedGradient | 0.867 | 0.055 | 0.046 |
| ThresholdOptimizer | 0.876 | 0.021 | 0.050 |

ThresholdOptimizer logró reducir la diferencia de paridad demográfica respecto del modelo base, aunque aumentó la diferencia de equalized odds.

## Explicabilidad

Se aplicó SHAP para analizar la influencia de las variables sobre las predicciones del modelo base.

Las características más influyentes fueron RecruitmentStrategy, SkillScore, EducationLevel e InterviewScore. El atributo Gender tuvo una influencia relativamente baja en comparación con estas variables.

Los gráficos generados se encuentran en `outputs/` y las interpretaciones detalladas en `evidencias.md`.

## Ejecución

El proyecto utiliza el entorno de la Unidad 2 de la plantilla de la cátedra.

1. Crear un Codespace con la configuración `unidad2-seminario-cd2`.
2. Ubicarse en la carpeta `unidad2/`.
3. Copiar `.env.example` a `.env`.
4. Configurar las variables del dataset.
5. Ejecutar:

```bash
python -m src.main
```

Las dependencias están especificadas en `requirements.txt`.

El dataset debe colocarse en `data/recruitment_data.csv`.

La ejecución genera las métricas y gráficos en `evidencias.md` y `outputs/`, respectivamente.

## Referencias

- Dastin, J. (2018). *Amazon scraps secret AI recruiting tool that showed bias against women*. Reuters.
- El Kharoua, R. *Predicting Hiring Decisions in Recruitment Data*. Kaggle.
- Fairlearn: https://fairlearn.org/
- SHAP: https://shap.readthedocs.io/