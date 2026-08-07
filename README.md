# 🛠️ Taller 9: Simulación de Comité de Arquitectura

## 🎯 Objetivo

Presentar la solución arquitectónica final del cliente real ante un panel simulado de evaluación, defendiendo las decisiones de diseño tomadas durante el curso con base en vistas, buenas prácticas e investigación previa — y presentando un plan de implementación que traduzca la solución en fases ejecutables, para que el cliente se vaya con una ruta clara de "cómo" y no solo con el diseño.

---

## 📘 Guía paso a paso

Antes de preparar la presentación, revise la [**Guía Paso a Paso: Simulación de Comité de Arquitectura**](clase/guia_paso_a_paso_presentacion.md). Incluye de qué taller se alimenta cada parte de la narrativa, la metodología de 6 pasos para pasar de todo el trabajo del curso a una presentación de 10 minutos defendible (incluyendo cómo construir el plan de implementación), un ejemplo completo (narrativa, matriz de riesgos, roadmap y preguntas anticipadas) sobre el caso de FarmApp, y una tabla de errores comunes.

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
3. Construya la matriz de riesgos arquitectónicos, consolidando los hallazgos de Infraestructura, STRIDE y Normatividad.
4. Construya el plan de implementación: traduzca la solución en fases (quick win, corto, mediano y largo plazo), cada una trazada a un riesgo específico.
5. Anticipe las preguntas críticas del panel y prepare respuestas basadas en evidencia.
6. Ensaye contra el tiempo (máximo 10 minutos) y valide con la [checklist de autoevaluación](clase/guia_paso_a_paso_presentacion.md#5-checklist-de-autoevaluación-antes-de-entregar).

- Asista a las presentaciones de otros equipos y prepare retroalimentación (peer review).

---

## 🧠 Parte 2: Entrega Final

Después de la presentación, el equipo debe:

- Ajustar la solución si recibió retroalimentación crítica.
- Consolidar todas las vistas y modelos en `entrega/vistas-finales/`.
- Entregar el resumen ejecutivo en `entrega/resumen-ejecutivo.md` usando la [plantilla de resumen ejecutivo](plantillas/plantilla_resumen_ejecutivo.md), y la matriz de evaluación de riesgos arquitectónicos (Paso 3 de la guía) en `presentacion/matriz-evaluacion.xlsx`.
- Entregar el plan de implementación en `entrega/plan-implementacion.md` usando la [plantilla de plan de implementación](plantillas/plantilla_plan_implementacion.md) (Paso 4 de la guía): fases, riesgo que corrige cada una, esfuerzo, duración y responsable sugerido.
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
│   ├── vistas-finales/                    # carpeta con diagramas consolidados
│   └── reflexiones/
│       ├── integrante1.md                 # Ver plantillas/plantilla_reflexion_integrante1.md
│       ├── integrante2.md
│       └── ...
└── plantillas/
    ├── plantilla_resumen_ejecutivo.md
    ├── plantilla_plan_implementacion.md
    └── plantilla_reflexion_integrante1.md
```

---

## ⚠️ Errores comunes

Antes de presentar, compare su narrativa, matriz y plan de implementación contra los errores más frecuentes (mostrar todos los diagramas del curso, matriz de riesgos hecha desde cero, solución sin plan de implementación, fases ordenadas solo por riesgo sin considerar esfuerzo) documentados en la [sección 4 de la guía paso a paso](clase/guia_paso_a_paso_presentacion.md#4-errores-comunes-a-evitar).

## 📤 Entregables

- Presentación ejecutiva (PDF o PowerPoint)
- Matriz de riesgos arquitectónicos
- Plan de implementación (roadmap de transición por fases)
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
| Presentación ejecutiva              | Clara, bien estructurada, ajustada al tiempo                            | Desordenada o confusa                                    |
| Reflexión individual                | Aporta valor personal sobre el proceso de aprendizaje                    | Superficial o repetitiva                                 |

---

## ✅ Licencia

Este taller hace parte del curso de Arquitectura Empresarial - Universidad de La Sabana. Uso académico bajo licencia MIT.
