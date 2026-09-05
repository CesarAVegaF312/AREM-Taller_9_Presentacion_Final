# 🛠️ Taller 9: Simulación de Comité de Arquitectura

## 🎯 Objetivo

Presentar la solución arquitectónica final del cliente real ante un panel simulado de evaluación, defendiendo las decisiones de diseño tomadas durante el curso con base en vistas, buenas prácticas e investigación previa — presentando un plan de implementación que traduzca la solución en fases ejecutables, y dejando definidos los mecanismos de gobernanza y el procedimiento de actualización de la arquitectura, para que el cliente se vaya con una ruta clara de "cómo" y de "qué pasa después", no solo con el diseño.

---

## 📘 Guía paso a paso

Antes de preparar la presentación, revise la [**Guía Paso a Paso: Simulación de Comité de Arquitectura**](clase/guia_paso_a_paso_presentacion.md). Incluye de qué taller se alimenta cada parte de la narrativa, la metodología de 6 pasos para pasar de todo el trabajo del curso a una presentación de 10 minutos defendible (incluyendo cómo construir el plan de implementación), un ejemplo completo (narrativa, matriz de riesgos, roadmap y preguntas anticipadas) sobre el caso de FarmApp, y una tabla de errores comunes.

### 🖼️ Versión visual: Hoja de cierre y gobernanza

[`clase/visualizacion-presentacion-final.html`](clase/visualizacion-presentacion-final.html) es una página interactiva autocontenida sobre el ejemplo guiado de FarmApp: una cadena clickeable con los 4 actos del pitch (Problema/Análisis/Solución/Plan de Implementación) mostrando de qué taller sale la evidencia de cada uno, otra cadena con las 3 preguntas de defensa anticipadas (pregunta/evidencia/respuesta), los 4 principios arquitectónicos y las 2 ADR reales (sincronización CDC y balanceador redundante), y la matriz de riesgos de 7 dominios junto con el plan de gobernanza y el procedimiento de actualización. GitHub no la renderiza interactiva desde la vista de archivo; para verla:
- Descargue el archivo y ábralo con doble clic (funciona sin conexión, es HTML plano), o
- Pegue esta URL en [htmlpreview.github.io](https://htmlpreview.github.io/): `https://raw.githubusercontent.com/CesarAVegaF312/AREM-Taller_9_Presentacion_Final/main/clase/visualizacion-presentacion-final.html`

## 🎓 Contexto del Taller

En este taller final, cada equipo debe presentar la solución arquitectónica completa diseñada para su cliente real. Se espera que articulen de forma clara las decisiones tomadas, las vistas generadas durante el curso y cómo estas responden a los objetivos estratégicos identificados. El panel de evaluación simula un comité técnico de arquitectura, como ocurre en ambientes corporativos reales, y busca evaluar tanto la solidez técnica como la capacidad argumentativa y comunicativa del equipo. Este espacio de simulación es clave para consolidar el aprendizaje aplicado del curso.

Durante la presentación se evaluarán:

- Coherencia entre las vistas desarrolladas
- Conexión con objetivos estratégicos del cliente
- Suficiencia técnica y argumentación
- Viabilidad del plan de implementación propuesto
- Respuesta a preguntas críticas

---

## 🧪 Parte 1: Trabajo en Clase

Durante la clase se espera que el equipo:

Siga la metodología de 6 pasos de la [guía paso a paso](clase/guia_paso_a_paso_presentacion.md) para preparar la presentación ejecutiva:

1. Estructure la narrativa en 4 actos: problema → análisis → solución → plan de implementación.
2. Seleccione la evidencia clave de cada taller anterior para cada acto.
3. Construya la matriz de riesgos arquitectónicos, consolidando los hallazgos de Infraestructura, STRIDE y Normatividad, y cubriendo además los dominios de Negocio y Datos/Procesos (7 dominios de riesgo de arquitectura empresarial).
4. Construya el plan de implementación: traduzca la solución en fases (quick win, corto, mediano y largo plazo), cada una trazada a un riesgo específico.
5. Anticipe las preguntas críticas del panel y prepare respuestas basadas en evidencia.
6. Ensaye contra el tiempo (máximo 10 minutos) y valide con la [checklist de autoevaluación](clase/guia_paso_a_paso_presentacion.md#5-checklist-de-autoevaluación-antes-de-entregar).
7. Defina los Principios Arquitectónicos, los Estándares tecnológicos y al menos 2 ADR reales del proyecto (sección 6.0 de la guía) — no se limite a diligenciar una plantilla en blanco.

- Asista a las presentaciones de otros equipos y prepare retroalimentación (peer review).

---

## 🧠 Parte 2: Entrega Final

Después de la presentación, el equipo debe:

- Ajustar la solución si recibió retroalimentación crítica.
- Consolidar todas las vistas y modelos en `entrega/vistas-finales/`.
- Entregar el resumen ejecutivo en `entrega/resumen-ejecutivo.md` usando la [plantilla de resumen ejecutivo](plantillas/plantilla_resumen_ejecutivo.md), y la matriz de evaluación de riesgos arquitectónicos (Paso 3 de la guía) en `presentacion/matriz-evaluacion.xlsx`.
- Entregar el plan de implementación en `entrega/plan-implementacion.md` usando la [plantilla de plan de implementación](plantillas/plantilla_plan_implementacion.md) (Paso 4 de la guía): fases, riesgo que corrige cada una, esfuerzo, duración y responsable sugerido.
- Entregar el plan de gobernanza en `entrega/plan-gobernanza.md` usando la [plantilla de plan de gobernanza](plantillas/plantilla_plan_gobernanza.md) (secciones 6.0 y 6.2 de la guía): principios arquitectónicos y estándares tecnológicos del proyecto, además de quién supervisa la ejecución del roadmap y con qué criterio.
- Entregar el procedimiento de actualización en `entrega/procedimiento-cambios.md` usando la [plantilla de procedimiento de cambios](plantillas/plantilla_procedimiento_cambios.md) (sección 6.3 de la guía): disparadores de cambio, proceso, y al menos 2 ADR reales del proyecto ya tomados (no una plantilla en blanco).
- Incluir una reflexión individual de cada integrante en `entrega/reflexiones/`, usando la [plantilla de reflexión](plantillas/plantilla_reflexion_integrante1.md) como base.

---

## 📁 Estructura esperada del repositorio

```text
taller-09-presentacion-final/
├── README.md
├── clase/
│   └── guia_paso_a_paso_presentacion.md   # De qué taller se alimenta cada acto, metodología y ejemplo guiado
├── presentacion/
│   ├── slides.pdf / pptx
│   └── matriz-evaluacion.pdf / .xlsx
├── entrega/
│   ├── resumen-ejecutivo.md               # Ver plantillas/plantilla_resumen_ejecutivo.md
│   ├── plan-implementacion.md             # Ver plantillas/plantilla_plan_implementacion.md
│   ├── plan-gobernanza.md                 # Ver plantillas/plantilla_plan_gobernanza.md
│   ├── procedimiento-cambios.md           # Ver plantillas/plantilla_procedimiento_cambios.md
│   ├── vistas-finales/                    # carpeta con diagramas consolidados
│   └── reflexiones/
│       ├── integrante1.md                 # Ver plantillas/plantilla_reflexion_integrante1.md
│       ├── integrante2.md
│       └── ...
└── plantillas/
    ├── plantilla_resumen_ejecutivo.md
    ├── plantilla_plan_implementacion.md
    ├── plantilla_plan_gobernanza.md
    ├── plantilla_procedimiento_cambios.md
    └── plantilla_reflexion_integrante1.md
```

---

## ⚠️ Errores comunes

Antes de presentar, compare su narrativa, matriz y plan de implementación contra los errores más frecuentes (mostrar todos los diagramas del curso, matriz de riesgos hecha desde cero, solución sin plan de implementación, fases ordenadas solo por riesgo sin considerar esfuerzo) documentados en la [sección 4 de la guía paso a paso](clase/guia_paso_a_paso_presentacion.md#4-errores-comunes-a-evitar).

## 📤 Entregables

- Presentación ejecutiva (PDF o PowerPoint)
- Matriz de riesgos arquitectónicos
- Plan de implementación (roadmap de transición por fases)
- Plan de gobernanza de la implementación
- Procedimiento de actualización y revisión de la arquitectura
- Documento resumen ejecutivo
- Vistas arquitectónicas finales
- Reflexiones individuales por integrante

---

## 📊 Rúbrica de Evaluación

| Criterio                            | Excelente (5)                                                           | Aceptable (3) / Insuficiente (1–2)                     |
|-------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------|
| Coherencia entre vistas             | Conexión clara y justificada entre las capas de arquitectura            | Fragmentado o sin vínculo entre componentes              |
| Argumentación y defensa técnica     | Explicación sólida y fundamentada de las decisiones de diseño            | Explicaciones débiles o improvisadas                     |
| Plan de implementación              | Fases claras, trazables a riesgos concretos, con esfuerzo y tiempos realistas | Fases genéricas o sin relación con los riesgos identificados |
| Gobernanza y gestión de cambios     | Principios arquitectónicos y estándares justificados en el proyecto, al menos 2 ADR reales bien argumentados, mecanismo de supervisión, criterios de conformidad y proceso de cambio claros y aplicables | Principios/estándares genéricos de manual, ADR sin llenar o hipotéticos, documentos copiados o sin relación con el proyecto |
| Presentación ejecutiva              | Clara, bien estructurada, ajustada al tiempo                            | Desordenada o confusa                                    |
| Reflexión individual                | Aporta valor personal sobre el proceso de aprendizaje                    | Superficial o repetitiva                                 |

---

## ✅ Licencia

Este taller hace parte del curso de Arquitectura Empresarial - Universidad de La Sabana. Uso académico bajo licencia MIT.
