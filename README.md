# Taller 9: Simulación de Comité de Arquitectura

## Objetivo

Presentar la solución arquitectónica final del cliente real ante un panel simulado de evaluación, defendiendo las decisiones de diseño tomadas durante el curso con base en vistas, buenas prácticas e investigación previa — presentando un plan de implementación que traduzca la solución en fases ejecutables, y dejando definidos los mecanismos de gobernanza y el procedimiento de actualización de la arquitectura, para que el cliente se vaya con una ruta clara de "cómo" y de "qué pasa después", no solo con el diseño.

---

## Guía paso a paso

Antes de preparar la presentación, revise la [**Guía Paso a Paso: Simulación de Comité de Arquitectura**](clase/guia_paso_a_paso_presentacion.md). Incluye de qué taller se alimenta cada parte de la narrativa, la metodología de 6 pasos para pasar de todo el trabajo del curso a una presentación de 10 minutos defendible (incluyendo cómo construir el plan de implementación), un ejemplo completo (narrativa, matriz de riesgos, roadmap y preguntas anticipadas) sobre el caso de FarmApp, y una tabla de errores comunes.

La presentación de la clase está en [`8. Gobierno_Arquitectura.pptx`](8.%20Gobierno_Arquitectura.pptx) (versión para estudiantes, sin notas del orador).

### Versión visual: Hoja de cierre y gobernanza

[`clase/visualizacion-presentacion-final.html`](clase/visualizacion-presentacion-final.html) es una página interactiva autocontenida sobre el ejemplo guiado de FarmApp: una cadena clickeable con los 4 actos del pitch (Problema/Análisis/Solución/Plan de Implementación) mostrando de qué taller sale la evidencia de cada uno, otra cadena con las 3 preguntas de defensa anticipadas (pregunta/evidencia/respuesta), los 4 principios arquitectónicos y las 2 ADR reales (sincronización CDC y balanceador redundante), y la matriz de riesgos de 7 dominios junto con el plan de gobernanza y el procedimiento de actualización. GitHub no la renderiza interactiva desde la vista de archivo; para verla:
- Descargue el archivo y ábralo con doble clic (funciona sin conexión, es HTML plano), o
- Pegue esta URL en [htmlpreview.github.io](https://htmlpreview.github.io/): `https://raw.githubusercontent.com/CesarAVegaF312/AREM-Taller_9_Presentacion_Final/main/clase/visualizacion-presentacion-final.html`

## Contexto del Taller

En este taller final, cada equipo debe presentar la solución arquitectónica completa diseñada para su cliente real. Se espera que articulen de forma clara las decisiones tomadas, las vistas generadas durante el curso y cómo estas responden a los objetivos estratégicos identificados. El panel de evaluación simula un comité técnico de arquitectura, como ocurre en ambientes corporativos reales, y busca evaluar tanto la solidez técnica como la capacidad argumentativa y comunicativa del equipo. Este espacio de simulación es clave para consolidar el aprendizaje aplicado del curso.

Durante la presentación se evaluarán:

- Coherencia entre las vistas desarrolladas
- Conexión con objetivos estratégicos del cliente
- Suficiencia técnica y argumentación
- Viabilidad del plan de implementación propuesto
- Respuesta a preguntas críticas

---

## Parte 1: Trabajo en Clase

Durante la clase se espera que el equipo:

Siga la metodología de 6 pasos de la [guía paso a paso](clase/guia_paso_a_paso_presentacion.md) para preparar la presentación ejecutiva:

1. Estructure la narrativa en 4 actos: problema → análisis → solución → plan de implementación.
2. Seleccione la evidencia clave de cada taller anterior para cada acto.
3. Construya la matriz de riesgos arquitectónicos, consolidando los hallazgos de Infraestructura, STRIDE y Normatividad, y cubriendo además los dominios de Negocio y Datos/Procesos (7 dominios de riesgo de arquitectura empresarial).
4. Construya el plan de implementación: traduzca la solución en fases (quick win, corto, mediano y largo plazo), cada una trazada a un riesgo específico.
5. Anticipe las preguntas críticas del panel y prepare respuestas basadas en evidencia.
6. Ensaye contra el tiempo (máximo 10 minutos) y valide con la [checklist de autoevaluación](clase/guia_paso_a_paso_presentacion.md#5-checklist-de-autoevaluación-antes-de-entregar).
7. Confirme, reescriba o retire los principios del borrador de la Visión del Taller 0 con la evidencia de los talleres intermedios, y defina los Estándares tecnológicos y al menos 2 ADR reales del proyecto (sección 6.0 de la guía) — no se limite a diligenciar una plantilla en blanco. Cada principio debe permitir decir «no» a algo concreto, cada estándar debe declarar su razón, y cada ADR debe incluir las alternativas descartadas y consecuencias negativas (reglas de calidad en la misma sección, tomadas del Módulo 8 de Gobierno de Arquitectura; el método de decisión con matriz ponderada se trabaja en el Taller 7).

8. Agregue al plan de implementación la **gestión del cambio con las personas** (Paso 4.1 de la guía): quién pierde o teme algo con cada fase, qué resistencia se espera, cómo se comunica y se capacita, y qué resultado visible deja cada fase, comprobado por alguien fuera de TI.
9. Agregue al plan de gobernanza **3 métricas de gobierno** (sección 6.2.1 de la guía), cada una con fórmula, fuente que ya existe, línea base y umbral, y una que mida al propio comité.

Los pasos 8 y 9 se trabajan en la sesión del **31/10** y no son entregables nuevos: van dentro de `plan-implementacion.md` y `plan-gobernanza.md`, con los mismos pesos (15% y 10%).

- Asista a las presentaciones de otros equipos y prepare retroalimentación (peer review).

---

## Parte 2: Entrega Final

La presentación es el **sábado 14/11** (ver [Sustentación final y evaluación del Corte 3](#sustentación-final-y-evaluación-del-corte-3)). El paquete final, ya ajustado con la retroalimentación del panel, se entrega hasta el **martes 17/11**. Después de la presentación, el equipo debe:

- Ajustar la solución si recibió retroalimentación crítica.
- Consolidar todas las vistas y modelos en `entrega/vistas-finales/`, incluyendo las dos vistas ArchiMate obligatorias (sección 7 de la guía): `archimate-motivacion` (objetivos del cliente → principios → requerimientos) y `archimate-migracion` (Gap → Work Package → Plateau TO-BE). Pueden hacerse en Archi (exportar también a PNG) o en draw.io con la biblioteca "ArchiMate 3"; la notación está en la [Guía de Notación ArchiMate](https://github.com/CesarAVegaF312/AREM-ArchiMate/blob/main/guia_notacion_archimate.md).
- Entregar el resumen ejecutivo en `entrega/resumen-ejecutivo.md` usando la [plantilla de resumen ejecutivo](plantillas/plantilla_resumen_ejecutivo.md), y la matriz de riesgos arquitectónicos (Paso 3 de la guía) en `presentacion/matriz-riesgos.xlsx` usando la [plantilla de matriz de riesgos](plantillas/plantilla_matriz_riesgos.xlsx). La metodología de los 7 dominios está en la *Guía Metodológica para el Análisis de Riesgos en Arquitectura Empresarial*, en [`clase/Guia_Metodologica_Analisis_Riesgos.pdf`](clase/Guia_Metodologica_Analisis_Riesgos.pdf).
- Entregar la retroalimentación del cliente en `entrega/retroalimentacion-cliente.md` (o escaneada en PDF), diligenciada y firmada por el cliente con la [plantilla de retroalimentación del cliente](plantillas/plantilla_retroalimentacion_cliente.md).
- Entregar el plan de implementación en `entrega/plan-implementacion.md` usando la [plantilla de plan de implementación](plantillas/plantilla_plan_implementacion.md) (Paso 4 de la guía): fases, riesgo que corrige cada una, esfuerzo, duración y responsable sugerido.
- Entregar el plan de gobernanza en `entrega/plan-gobernanza.md` usando la [plantilla de plan de gobernanza](plantillas/plantilla_plan_gobernanza.md) (secciones 6.0, 6.2 y 6.2.1 de la guía): principios arquitectónicos y estándares tecnológicos del proyecto, métricas de gobierno, además de quién supervisa la ejecución del roadmap y con qué criterio.
- Entregar el procedimiento de actualización en `entrega/procedimiento-cambios.md` usando la [plantilla de procedimiento de cambios](plantillas/plantilla_procedimiento_cambios.md) (sección 6.3 de la guía): disparadores de cambio, proceso, y al menos 2 ADR reales del proyecto ya tomados (no una plantilla en blanco).
- Incluir una reflexión individual de cada integrante en `entrega/reflexiones/`, usando la [plantilla de reflexión](plantillas/plantilla_reflexion_integrante1.md) como base.
- Cada integrante envía, **de forma individual y privada** por el Aula Virtual (no en el repositorio), su coevaluación con la [plantilla de coevaluación](plantillas/plantilla_coevaluacion.md).

---

## Estructura esperada del repositorio

```text
taller-09-presentacion-final/
├── README.md
├── clase/
│   └── guia_paso_a_paso_presentacion.md   # De qué taller se alimenta cada acto, metodología y ejemplo guiado
├── presentacion/
│   ├── slides.pdf / pptx
│   └── matriz-riesgos.xlsx                # Ver plantillas/plantilla_matriz_riesgos.xlsx
├── entrega/
│   ├── resumen-ejecutivo.md               # Ver plantillas/plantilla_resumen_ejecutivo.md
│   ├── plan-implementacion.md             # Ver plantillas/plantilla_plan_implementacion.md
│   ├── plan-gobernanza.md                 # Ver plantillas/plantilla_plan_gobernanza.md
│   ├── procedimiento-cambios.md           # Ver plantillas/plantilla_procedimiento_cambios.md
│   ├── retroalimentacion-cliente.md       # Ver plantillas/plantilla_retroalimentacion_cliente.md (firmada)
│   ├── vistas-finales/                    # carpeta con diagramas consolidados
│   │   ├── archimate-motivacion.(archimate|drawio) + .png
│   │   └── archimate-migracion.(archimate|drawio) + .png
│   └── reflexiones/
│       ├── integrante1.md                 # Ver plantillas/plantilla_reflexion_integrante1.md
│       ├── integrante2.md
│       └── ...
└── plantillas/
    ├── plantilla_resumen_ejecutivo.md
    ├── plantilla_matriz_riesgos.xlsx
    ├── plantilla_plan_implementacion.md
    ├── plantilla_plan_gobernanza.md
    ├── plantilla_procedimiento_cambios.md
    ├── plantilla_retroalimentacion_cliente.md
    ├── plantilla_coevaluacion.md          # Se envía privada por Aula Virtual, no se sube al repo
    └── plantilla_reflexion_integrante1.md
```

En el repositorio del proyecto del equipo (`AREM-EquipoX-NombreCliente`, ver [`AREM-Proyecto-Cliente`](https://github.com/CesarAVegaF312/AREM-Proyecto-Cliente)) todo lo anterior va **plano** dentro de `09-presentacion-final/`, sin las subcarpetas `entrega/` y `presentacion/`: `09-presentacion-final/plan-implementacion.md`, `09-presentacion-final/matriz-riesgos.xlsx`, `09-presentacion-final/presentacion.pdf` (las diapositivas), `09-presentacion-final/vistas-finales/`, etc. El resumen ejecutivo se copia además a la raíz como `resumen-ejecutivo.md`; sus enlaces ya asumen esta estructura.

---

## Errores comunes

Antes de presentar, compare su narrativa, matriz y plan de implementación contra los errores más frecuentes (mostrar todos los diagramas del curso, matriz de riesgos hecha desde cero, solución sin plan de implementación, fases ordenadas solo por riesgo sin considerar esfuerzo) documentados en la [sección 4 de la guía paso a paso](clase/guia_paso_a_paso_presentacion.md#4-errores-comunes-a-evitar).

## Entregables

- Presentación ejecutiva (PDF o PowerPoint)
- Matriz de riesgos arquitectónicos
- Plan de implementación (roadmap de transición por fases)
- Plan de gobernanza de la implementación
- Procedimiento de actualización y revisión de la arquitectura
- Documento resumen ejecutivo
- Vistas arquitectónicas finales, incluyendo las vistas ArchiMate de Motivación y de Implementación y Migración
- Retroalimentación del cliente, firmada
- Reflexiones individuales por integrante
- Coevaluación individual (privada, por Aula Virtual)

---

## Sustentación final y evaluación del Corte 3

**Fechas**

| Fecha | Qué pasa |
|---|---|
| Sábado 07/11 | Ensayo con el docente: presentación completa cronometrada |
| Sábado 14/11 | Sustentación final ante el panel y el cliente |
| Martes 17/11 | Plazo de entrega del paquete final ajustado (repositorio del equipo) |

**Formato de la sustentación**

- Presentación de máximo 10 minutos con los 4 actos de la [guía](clase/guia_paso_a_paso_presentacion.md#2-metodología-en-6-pasos), seguida de preguntas del panel.
- **El cliente real debe asistir**, de forma presencial o virtual. El equipo coordina con anticipación la conexión del cliente si asiste virtualmente. Si a última hora el cliente no puede asistir, el equipo debe entregar de todas formas la retroalimentación del cliente firmada (ver plantilla) y avisar al docente antes de la sustentación.
- Todos los integrantes presentan una parte y deben poder responder preguntas sobre cualquier sección.

**Distribución del 25% del Corte 3 (componente de Proyecto)**

| Componente | Peso dentro del corte | Dónde se evalúa |
|---|---|---|
| Taller 7: documento de mejora de arquitectura + TO-BE + matriz de brechas | 25% | Rúbrica del Taller 7 |
| Taller 8: tablero integrado + informe | 10% | Rúbrica del Taller 8 |
| Sustentación ante el panel (presentación + defensa) | 25% | Rúbrica de este taller: coherencia, argumentación y presentación ejecutiva |
| Matriz de riesgos + plan de implementación (incluye gestión del cambio) | 15% | Rúbrica de este taller: matriz de riesgos y plan de implementación |
| Gobernanza + procedimiento de cambios (principios, estándares, métricas, ADR) | 10% | Rúbrica de este taller: gobernanza y gestión de cambios |
| Vistas ArchiMate (motivación + migración) | 5% | Rúbrica de este taller: vistas ArchiMate |
| Retroalimentación del cliente (formato firmado) | 5% | Proporcional al promedio de la valoración 1-5 que pone el cliente en la plantilla: `5% × promedio / 5`. Sin formato firmado, 0 |
| Reflexión individual | 5% | Rúbrica de este taller: reflexión individual (nota individual) |

**Coevaluación:** no tiene peso propio. Se aplica como un factor individual entre 0,8 y 1,0 sobre la nota grupal de cada integrante, calculado a partir de la coevaluación que hacen sus compañeros de equipo: `factor = mín(1,0 ; 0,8 + 0,2 × (promedio − 1) / 3)`, donde `promedio` es la calificación promedio (1 a 5) que recibió de sus compañeros. Un promedio de 4 o más conserva el 100% de la nota grupal; un promedio de 1 deja el 80%.

---

## Rúbrica de Evaluación

| Criterio                            | Excelente (5)                                                           | Aceptable (3) / Insuficiente (1–2)                     |
|-------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------|
| Coherencia entre vistas             | Conexión clara y justificada entre las capas de arquitectura            | Fragmentado o sin vínculo entre componentes              |
| Argumentación y defensa técnica     | Explicación sólida y fundamentada de las decisiones de diseño            | Explicaciones débiles o improvisadas                     |
| Matriz de riesgos                   | Consolida los hallazgos de los Talleres 4, 5 y 6 sin rehacerlos, cubre los 7 dominios (al menos Negocio y Datos/Procesos además de los técnicos), con nivel calculado, prioridad justificada y una estrategia explícita por riesgo (eliminar, reducir, transferir o aceptar) con al menos un riesgo aceptado y justificado | Riesgos inventados o sin taller de origen, solo riesgos técnicos, prioridad sin relación con impacto y probabilidad, o riesgos sin estrategia (aceptados sin decirlo) |
| Plan de implementación              | Fases claras, trazables a riesgos concretos, con esfuerzo y tiempos realistas; gestión del cambio con los grupos afectados reales y un resultado visible por fase | Fases genéricas o sin relación con los riesgos identificados; sin gestión del cambio o con grupos genéricos |
| Gobernanza y gestión de cambios     | Principios arquitectónicos y estándares justificados en el proyecto, al menos 2 ADR reales bien argumentados, mecanismo de supervisión, criterios de conformidad, 3 métricas calculables (fórmula, fuente, línea base, umbral) y proceso de cambio claros y aplicables | Principios/estándares genéricos de manual, ADR sin llenar o hipotéticos, métricas sin fórmula o sin umbral, documentos copiados o sin relación con el proyecto |
| Presentación ejecutiva              | Clara, bien estructurada, ajustada al tiempo                            | Desordenada o confusa                                    |
| Vistas ArchiMate                    | La vista de Motivación conecta los objetivos de la Ficha con los principios y requerimientos; la vista de Migración muestra cada fase del plan como Work Package que resuelve un Gap del Taller 7 y produce el Plateau TO-BE, con notación correcta | Falta una de las dos vistas, notación incorrecta o elementos sin relación con el plan de implementación |
| Reflexión individual                | Aporta valor personal sobre el proceso de aprendizaje                    | Superficial o repetitiva                                 |

---

## Licencia

Este taller hace parte del curso de Arquitectura Empresarial - Universidad de La Sabana. Uso académico bajo licencia MIT.
