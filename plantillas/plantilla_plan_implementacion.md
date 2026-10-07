# Plan de Implementación (Roadmap de Transición)

## Cliente
_Escriba aquí el nombre del cliente real al que se le aplicó el análisis arquitectónico._

## Integrantes del equipo
- Nombre 1 (correo o usuario GitHub)
- Nombre 2
- Nombre 3

## Propósito de este documento

Explique en 2-3 líneas qué solución arquitectónica se va a implementar (Acto 3 de la presentación) y por qué el cliente necesita un plan de implementación además del diseño — es decir, qué pasaría si solo se entregara el diseño sin una ruta clara de ejecución.

## Fases de implementación

Traduzca la solución en fases ejecutables. Cada fase debe estar trazada a un riesgo de la matriz de riesgos (`matriz-riesgos.xlsx`, Taller 9 Paso 3) o a una brecha de la matriz de brechas del Taller 7 — sea de Infraestructura (Taller 4), Seguridad (Taller 5), Normatividad (Taller 6) o de los dominios de Negocio, Procesos y Datos. No invente fases sin relación con hallazgos previos del curso. Cada fase será además un Work Package en la vista ArchiMate de migración (guía, sección 7.1).

| Fase | Qué se implementa | Riesgo / brecha que corrige | Esfuerzo (Bajo/Medio/Alto) | Duración estimada | Responsable sugerido |
|---|---|---|---|---|---|
| Quick win | | | | | |
| Corto plazo | | | | | |
| Mediano plazo | | | | | |
| Largo plazo | | | | | |

> **Recuerde:** el orden de las fases no depende solo de la prioridad de riesgo (Taller 9, Paso 3) — un riesgo de alta prioridad pero de alto esfuerzo no necesariamente va primero. Cruce prioridad de riesgo con esfuerzo de implementación al secuenciar.

## Línea de tiempo

Represente la línea de tiempo de las fases anteriores. Puede usar un diagrama de Gantt en Mermaid (se renderiza solo en GitHub) o una tabla/imagen equivalente:

```mermaid
gantt
    title Roadmap de Implementación
    dateFormat YYYY-MM-DD
    axisFormat %b
    section Quick win
    Nombre de la tarea :qw1, 2026-01-01, 30d
    section Corto plazo
    Nombre de la tarea :cp1, 2026-02-01, 60d
    section Mediano plazo
    Nombre de la tarea :mp1, 2026-04-01, 90d
    section Largo plazo
    Nombre de la tarea :lp1, 2026-07-01, 180d
```

## Dependencias entre fases

Indique si alguna fase requiere que otra termine primero (ej. "la sincronización en tiempo real depende de que el proveedor de nube confirme la capacidad adicional que se pidió en la fase de corto plazo").

## Gestión del cambio con las personas

Ver el Paso 4.1 de la guía. Liste de 3 a 5 grupos afectados por las fases (si el cliente es pequeño, 2 o 3), incluyendo siempre al grupo cuyo trabajo cambia o desaparece.

| Grupo | Qué pierde o teme | Resistencia esperada | Poder / interés (Alto / Medio / Bajo) | Comunicación y capacitación | Cuándo | Responsable |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Resultado visible por fase

Cada fase debe dejar un resultado que compruebe alguien del negocio, no de tecnología.

| Fase | Resultado visible | Quién lo comprueba (fuera de TI) |
|---|---|---|
| Quick win | | |
| Corto plazo | | |
| Mediano plazo | | |
| Largo plazo | | |

## Referencias

Cite aquí cualquier fuente sobre gestión de portafolios de proyectos, priorización o buenas prácticas de transición arquitectónica (ej. TOGAF ADM Fase E/F - Opportunities & Solutions / Migration Planning) que haya usado para construir este plan.

---

_Este documento hace parte de la entrega final del Taller 9 del curso AREM (Arquitectura Empresarial) - Universidad de La Sabana._
