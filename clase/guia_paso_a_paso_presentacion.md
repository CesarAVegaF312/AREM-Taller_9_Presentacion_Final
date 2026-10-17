# Guía Paso a Paso: Simulación de Comité de Arquitectura

Esta guía complementa el `README.md` del taller. A diferencia de los talleres anteriores, aquí no se construye una vista nueva ni se usa un caso base de clase: se toma **todo** el trabajo hecho para el cliente real (Talleres 1 a 8) y se condensa en una presentación ejecutiva de máximo 10 minutos, defendible ante un panel.

---

## 1. De dónde sale cada parte de la narrativa

La presentación se organiza en 4 actos. Cada uno se alimenta de talleres específicos — no se inventa contenido nuevo, se selecciona y se resume lo ya construido. El cuarto acto existe porque una solución sin plan de implementación deja al cliente con la misma pregunta sin responder: "¿y ahora cómo lo hago?".

| Acto | Pregunta que responde | Se alimenta de |
|---|---|---|
| 1. Problema | ¿Qué necesita el cliente y por qué es urgente? | Taller 1 (proceso actual), Taller 2 (modelo de información y diagrama de contexto) |
| 2. Análisis | ¿Cómo está hoy la arquitectura y qué riesgos tiene? | Taller 3 (C1/C2), Taller 4 (infraestructura), Taller 5 (STRIDE), Taller 6 (normatividad) |
| 3. Solución | ¿Qué se propone y por qué es la mejor alternativa? | Taller 7 (Opportunities & Solutions: TO-BE y brechas), Taller 8 (integración de vistas) |
| 4. Plan de Implementación | ¿Cómo y en qué orden se llega de lo actual a lo propuesto? | Riesgos priorizados (Paso 3 de esta guía) + Solución (Acto 3) |

---

## 2. Metodología en 6 pasos

1. **Estructurar la narrativa** — organice todo el trabajo del curso en la historia de 4 actos: problema → análisis → solución → plan de implementación.
2. **Seleccionar la evidencia clave por acto** — de cada vista ya construida, elija solo lo que sostiene ese punto de la narrativa; en 10 minutos no cabe todo.
3. **Construir la matriz de riesgos arquitectónicos** — consolide (no repita desde cero) los riesgos ya identificados en el curso (Infraestructura, STRIDE/Seguridad, Normatividad) y complételos con los dominios que un análisis puramente técnico suele dejar por fuera (Negocio, Procesos, Datos, Aplicaciones), siguiendo los 7 dominios de riesgo de arquitectura empresarial, priorizados en una sola matriz ejecutiva.
4. **Construir el plan de implementación** — traduzca la solución (Acto 3) en fases ejecutables (quick win, corto, mediano y largo plazo), cada una trazable a un riesgo o brecha específico del Paso 3, con esfuerzo, duración y responsable sugerido.
5. **Preparar la defensa** — anticipe las preguntas más probables del panel (incluyendo sobre la viabilidad del plan de implementación) y prepare una respuesta basada en evidencia del curso, no en opinión.
6. **Ensayar contra el tiempo y ajustar** — practique la presentación completa cronometrada y recorte contenido (no velocidad de habla) hasta que quepa en el tiempo asignado.

---

## 3. Ejemplo guiado: Defensa de la solución de FarmApp

Continuando el ejemplo del Taller 8 (el hilo de negocio "Compra Online" de FarmApp), así se vería la síntesis para el comité. FarmApp es un caso de clase: cuando el ejemplo dice que un hallazgo salió del Taller 4, 5 o 6, indica de qué taller saldría ese hallazgo en un cliente real.

### Paso 1 — Estructurar la narrativa

- **Acto 1 — Problema:** "FarmApp pierde ventas cuando el inventario del canal digital no refleja el inventario real de las tiendas físicas, generando pedidos que no se pueden despachar."
- **Acto 2 — Análisis:** "La arquitectura actual sincroniza el inventario entre el POS y la Plataforma E-commerce a través de la Base de Datos Replicada con varias horas de retraso; en horas pico, ese retraso es la causa raíz de los pedidos fallidos."
- **Acto 3 — Solución:** "Se propone sincronización casi en tiempo real (captura de cambios) entre el POS y la plataforma e-commerce, priorizada sobre alternativas más costosas por su menor impacto en el sistema heredado."
- **Acto 4 — Plan de Implementación:** "La solución se ejecuta en 4 fases, empezando por el ajuste de consentimiento legal (bajo esfuerzo, corrige una brecha de cumplimiento) y terminando por la redundancia del balanceador (esfuerzo medio, pero el riesgo de menor probabilidad)."

### Paso 2 — Seleccionar la evidencia clave por acto

| Acto | Vista de origen | Qué mostrar (un solo elemento, no todo el taller) |
|---|---|---|
| Problema | Vista de negocio (Taller 1 / 7) | El proceso "Compra Online" con el punto de falla resaltado |
| Análisis | Vista de infraestructura (Taller 4 / 7) | El mapa con el componente de sincronización marcado como cuello de botella |
| Solución | Tablero integrado (Taller 8) | La nueva conexión propuesta entre POS y la plataforma e-commerce |
| Plan de Implementación | Matriz de riesgos (Paso 3) | El roadmap de fases con su línea de tiempo (Paso 4) |

### Paso 3 — Construir la matriz de riesgos arquitectónicos

Las columnas siguen la plantilla oficial de la [Guía Metodológica de Análisis de Riesgos en Arquitectura Empresarial](Guia_Metodologica_Analisis_Riesgos.pdf) del curso — que también describe los 7 dominios (Negocio, Procesos, Datos, Aplicaciones, Infraestructura, Seguridad, Gobierno TI) con sus preguntas guía — y están listas en la [plantilla de matriz de riesgos](../plantillas/plantilla_matriz_riesgos.xlsx) (`Riesgo | Causa | Impacto | Probabilidad | Arquitectura afectada | Mitigación`), con una columna adicional `Prioridad` porque el Plan de Implementación (Paso 4) necesita un orden para secuenciar las fases. La plantilla agrega además `ID`, `Origen` (de qué taller sale), `Nivel` (impacto × probabilidad, calculado), `Estrategia` y `Control` (ver más abajo) y `Fase del plan que lo mitiga`. Las filas están ordenadas por prioridad: cuatro riesgos vienen de hallazgos ya identificados en talleres anteriores (Infraestructura, Seguridad y Gobierno TI); otros dos formalizan riesgos de Datos/Procesos y de Negocio que un análisis puramente técnico suele dejar por fuera; el séptimo es un riesgo de nivel bajo que se acepta de forma explícita y justificada.

> **Escala.** En la clase del 24/10 el Risk Storming usa una matriz cualitativa de 2×2. Para la entrega use la escala de la plantilla: Impacto Bajo / Medio / Alto / Crítico, Probabilidad Baja / Media / Alta, y Nivel de 1 a 12. Un riesgo es **crítico** cuando su Nivel es 8 o más (la plantilla lo marca en rojo). En «Arquitectura afectada» puede combinar dos dominios (por ejemplo «Datos / Procesos»), como en la Guía Metodológica.

> **Estrategia de respuesta y tipo de control.** Para cada riesgo escriba qué se decide hacer con él, con las cuatro estrategias del Módulo 9, de la más agresiva a la más pasiva: **Eliminar** (erradicar la fuente cambiando el proceso o el diseño), **Reducir** (bajar la probabilidad o el impacto con controles), **Transferir** (trasladar la consecuencia a un tercero: contrato con SLA y penalidades, póliza) o **Aceptar** (asumirlo porque mitigar cuesta más que el daño esperado). Aceptar es una decisión legítima siempre que sea explícita y quede registrada con su justificación; aceptar sin decirlo es no haber mirado, y por eso la plantilla exige al menos un riesgo aceptado. Para la mitigación indique además si el control es **preventivo** (actúa antes del evento y evita que ocurra) o **reactivo** (actúa después y reduce el daño): es el modelo **Bow-Tie**, con las causas a la izquierda del evento de riesgo y los efectos a la derecha. En FarmApp, el evento «la pasarela de pagos no responde» tiene como controles preventivos el contrato con SLA y el monitoreo del proveedor, y como controles reactivos el reintento asíncrono de la transacción y el proveedor alterno. La mayoría de los equipos solo dibuja el lado preventivo, y así el sistema queda sin plan para cuando el riesgo ocurre de todos modos.

| Riesgo | Causa | Impacto | Probabilidad | Arquitectura afectada | Mitigación | Estrategia | Control | Prioridad |
|---|---|---|---|---|---|---|---|---|
| Retraso de sincronización de inventario | Sincronización POS ↔ e-commerce mediante base de datos replicada con corte batch (Taller 4) | Alto | Alta | Infraestructura | Sincronización casi en tiempo real (CDC) entre POS y e-commerce | Reducir | Preventivo | 1 |
| Inventario desincronizado entre POS y e-commerce genera pedidos fallidos | Ausencia de un proceso de reconciliación y alertas de discrepancia entre el inventario del POS y el del e-commerce (el problema central del Acto 2) | Alto | Alta | Datos / Procesos | Proceso de reconciliación automática con alertas de discrepancia y trazabilidad de cada ajuste de stock | Reducir | Reactivo | 1 |
| Exposición de datos de pago | Falta de cifrado en tránsito en el flujo de pagos (Taller 5, STRIDE) | Alto | Media | Seguridad | TLS en todos los subdominios y cifrado de datos de pago en tránsito | Reducir | Preventivo | 2 |
| Incumplimiento de la Ley 1581 en el manejo de datos de clientes | Ausencia de consentimiento explícito antes de procesar datos personales/de pago (Taller 6, normatividad) | Alto | Media | Gobierno TI | Consentimiento explícito antes de procesar datos de pago | Eliminar | Preventivo | 2 |
| Dependencia de un único proveedor de logística para entregas | No existe un proveedor alterno contratado ni cláusulas de contingencia en el contrato actual | Alto | Media | Negocio | Contrato con proveedor de logística alterno y SLA de respaldo | Transferir | Reactivo | 2 |
| Punto único de falla en el balanceador de carga | Un único balanceador de carga activo, sin redundancia (Taller 4) | Alto | Baja | Infraestructura | Redundancia del balanceador de carga | Reducir | Preventivo | 3 |
| Reportes internos de ventas lentos en cierre de mes | Los reportes consultan la misma base de datos transaccional del POS (Taller 4) | Bajo | Baja | Infraestructura | Ninguna por ahora: se monitorea el tiempo de respuesta y se revisa si supera 30 s | Aceptar (Nivel 1, componente secundario: una réplica de lectura cuesta más que el daño esperado) | Reactivo | 4 |

> **Si la solución (Acto 3) incluye un agente de IA**, agregue aquí también sus riesgos propios (alucinación, prompt injection, autonomía sin supervisión, costo descontrolado) — vea el [patrón de sistemas agénticos](https://github.com/CesarAVegaF312/AREM-ArchiMate/blob/main/patron_sistemas_agenticos.md). Estos riesgos normalmente caen en el dominio "Aplicaciones" de esta matriz.

### Paso 4 — Construir el plan de implementación

Se traducen en fases ejecutables los riesgos del Paso 3 que requieren una intervención arquitectónica o técnica. No todos los 6 riesgos identificados ameritan una fase nueva del roadmap: la fase "Mediano plazo" (sincronización CDC) mitiga a la vez el riesgo de infraestructura y el de Datos/Procesos, porque ambos comparten la misma causa raíz; y el riesgo de Negocio (dependencia de un único proveedor de logística) se gestiona por vía contractual/de gobernanza — por eso se incorpora como disparador de cambio en el Procedimiento de Actualización (sección 6.3), no como una fase técnica de este roadmap. El orden de las 4 fases restantes no sigue la columna "Prioridad" al pie de la letra: el riesgo de mayor prioridad (retraso de sincronización) exige más esfuerzo de desarrollo, así que no es el quick win — se cruza prioridad de riesgo con esfuerzo de implementación.

| Fase | Qué se implementa | Riesgo que corrige | Esfuerzo | Duración | Responsable sugerido |
|---|---|---|---|---|---|
| Quick win | Consentimiento explícito antes de procesar datos de pago | Incumplimiento Ley 1581 | Bajo | 0–1 mes | Producto / Legal |
| Corto plazo | TLS en todos los subdominios y cifrado de datos de pago en tránsito | Exposición de datos de pago (STRIDE) | Medio | 1–3 meses | Seguridad |
| Mediano plazo | Sincronización casi en tiempo real (CDC) entre POS y e-commerce, con reconciliación automática y alertas de discrepancia | Retraso de sincronización de inventario e inventario desincronizado (Datos / Procesos) | Alto | 3–6 meses | Plataforma |
| Largo plazo | Redundancia del balanceador de carga | Punto único de falla | Medio | 6–12 meses | Infraestructura |

```mermaid
gantt
    title Roadmap de Implementación - FarmApp
    dateFormat YYYY-MM-DD
    axisFormat %b
    section Quick win
    Consentimiento explícito (Ley 1581) :done, qw1, 2026-01-01, 30d
    section Corto plazo
    TLS y cifrado de datos de pago :active, cp1, 2026-02-01, 60d
    section Mediano plazo
    Sincronización CDC POS-Ecommerce :mp1, 2026-04-01, 90d
    section Largo plazo
    Redundancia del balanceador :lp1, 2026-07-01, 180d
```

#### 4.1 Gestión del cambio con las personas

El roadmap anterior dice qué se construye y en qué orden, pero no quién tiene que cambiar su forma de trabajar para que funcione. Una solución técnicamente correcta fracasa igual si las personas que la usan siguen haciendo lo de antes "por si acaso". Este apartado no es la *Architecture Change Management* de la sección 6.3 (que trata de cómo se actualiza la **arquitectura** después): trata de cómo se lleva a **la gente** de lo actual a lo propuesto mientras se ejecuta el plan.

**Paso A — Identifique a quién le cambia el trabajo.** Liste de 3 a 5 grupos afectados por las fases del plan. Incluya siempre al grupo cuya tarea cambia o desaparece (en FarmApp, el personal de tienda que hoy ajusta inventario a mano), no solo a la dirección.

**Paso B — Diga qué pierde o teme cada grupo.** Cada grupo pierde algo, y eso es información: de ahí sale la resistencia que se espera, y de la resistencia sale la acción. Ubique a cada grupo en la rejilla de poder e interés (Alto / Medio / Bajo) para decidir con quién se negocia y a quién se informa.

**Paso C — Defina comunicación y capacitación, con fecha y responsable.** Las dos: comunicar sin capacitar deja a la gente sabiendo que algo cambia pero sin saber hacerlo.

| Grupo | Qué pierde o teme | Resistencia esperada | Poder / interés | Comunicación y capacitación | Cuándo | Responsable |
|---|---|---|---|---|---|---|
| Personal de tienda (cajeros POS) | Que el inventario en línea los haga responsables de cada descuadre | Seguir ajustando el stock a mano "por si acaso", lo que vuelve a desincronizar | Bajo / Alto | Explicar qué cambia en su cierre de caja; capacitación de 1 hora en el registro de ajustes de stock | Antes de la fase Mediano plazo | Operaciones de tiendas |
| Área comercial del e-commerce | Perder ventas durante las ventanas de corte del CDC | Presionar para que no haya ventanas de corte en temporada alta | Alto / Alto | Calendario de cortes acordado por adelantado; tablero de pedidos fallidos para ver el efecto | Antes de cada corte | Producto |
| Equipo de plataforma (soporte del POS heredado) | Que el CDC complique el soporte del POS | Dilatar la fase con dudas técnicas | Medio / Alto | Participar en la ADR #1; capacitación en el bus de eventos | Desde el quick win | Arquitecto líder |
| Gerencia general | Invertir sin ver resultados | Aprobar solo lo que muestre ahorro rápido | Alto / Medio | Un informe de una página por fase con el resultado visible, no con el porcentaje de avance | Al cierre de cada fase | Arquitecto líder |

**Paso D — Un resultado visible por fase, comprobado fuera de TI.** La urgencia no se construye con un discurso de lanzamiento sino con el primer resultado que alguien del negocio puede ver (adaptado de Kotter, 1996). Cada fase del plan debe dejar un resultado que compruebe alguien que no es de tecnología:

| Fase | Resultado visible | Quién lo comprueba (fuera de TI) |
|---|---|---|
| Quick win | Ningún pago se procesa sin consentimiento registrado | Legal |
| Corto plazo | El flujo de pagos pasa la revisión de seguridad sin hallazgos altos | Auditoría interna |
| Mediano plazo | Los pedidos fallidos por falta de stock bajan en horas pico | Área comercial |
| Largo plazo | La caída de un balanceador no detiene la venta en línea | Operaciones |

> Si su cliente es pequeño (un emprendimiento con 3 personas), la tabla puede tener solo 2 o 3 grupos — no invente áreas que no existen. Lo que no puede faltar es la persona cuyo trabajo cambia.

### Paso 5 — Preparar la defensa

> Vea la [versión visual interactiva](visualizacion-presentacion-final.html) de este pitch y de las preguntas de defensa (resume los Pasos 1, 3 y 5 y la sección 6; el plan, la gestión del cambio, las métricas y las vistas ArchiMate están solo en esta guía).

| Pregunta probable del panel | Respuesta basada en evidencia |
|---|---|
| "¿Por qué no migraron todo a la nube pública en vez de mantener la nube híbrida?" | "El Taller 4 identificó que los servidores regionales ya cumplen el SLA de latencia local; migrar todo implicaría reescribir el sistema POS heredado sin un beneficio claro a corto plazo." |
| "¿Cómo garantizan el cumplimiento de la Ley 1581 con el nuevo flujo de datos?" | "El Taller 6 identificó la brecha de consentimiento explícito; por eso es el quick win del plan de implementación, no algo pospuesto para el año siguiente." |
| "¿Por qué la corrección del mayor riesgo (sincronización de inventario) no es lo primero que hacen?" | "Es la fase de mayor esfuerzo de desarrollo; empezar por los quick wins de bajo esfuerzo genera confianza y resultados visibles mientras se prepara la fase más compleja." |

### Paso 6 — Ensayar contra el tiempo

| Sección | Tiempo objetivo |
|---|---|
| Acto 1 — Problema | 2 min |
| Acto 2 — Análisis | 2 min |
| Acto 3 — Solución | 2 min |
| Acto 4 — Plan de Implementación | 2 min |
| Cierre y transición a preguntas | 2 min |
| **Total** | **10 min** |

---

## 4. Errores comunes a evitar

| Error frecuente | Por qué es un problema | Cómo corregirlo |
|---|---|---|
| Mostrar todos los diagramas de los 8 talleres en la presentación | Se pierde el tiempo asignado en detalle irrelevante para el panel | Seleccione solo la evidencia que sostiene cada acto (Paso 2) |
| Matriz de riesgos hecha desde cero, sin relación con los hallazgos previos | Contradice o repite trabajo ya hecho en el curso | Consolide los riesgos ya identificados en los Talleres 4, 5 y 6, y cúbralos con los 7 dominios de riesgo de arquitectura empresarial (no solo Infraestructura, Seguridad y Normatividad) |
| Proponer una solución sin plan de implementación | El cliente se queda con el mismo "¿y ahora cómo lo hago?" que tenía antes del curso | Traduzca la solución en fases con esfuerzo, duración y responsable (Paso 4) |
| Ordenar las fases del plan solo por prioridad de riesgo | Un riesgo de alta prioridad pero alto esfuerzo no siempre debe ir primero | Cruce prioridad de riesgo con esfuerzo de implementación al secuenciar las fases |
| No practicar la defensa de preguntas difíciles | El equipo improvisa respuestas débiles frente al panel | Anticipe preguntas críticas y prepare respuestas basadas en evidencia (Paso 5) |
| Presentación sin cronometrar | Se corta a mitad de la solución por exceso de tiempo | Ensaye con cronómetro y ajuste el contenido, no la velocidad al hablar |

---

## 5. Checklist de autoevaluación antes de entregar

- [ ] La narrativa sigue la estructura problema → análisis → solución → plan de implementación.
- [ ] Cada acto muestra solo la evidencia esencial de las vistas ya construidas, no todos los diagramas.
- [ ] La matriz de riesgos consolida los hallazgos de Infraestructura, STRIDE y Normatividad, y cubre además los dominios de Negocio y Datos/Procesos (7 dominios de riesgo de arquitectura empresarial), con columnas Riesgo, Causa, Impacto, Probabilidad, Arquitectura afectada y Mitigación.
- [ ] Existe un plan de implementación con fases (quick win, corto, mediano y largo plazo), cada una trazada a un riesgo o brecha específico.
- [ ] El orden de las fases considera tanto el riesgo como el esfuerzo de implementación, no solo la prioridad de riesgo.
- [ ] El plan incluye la gestión del cambio con las personas (Paso 4.1): grupos afectados con lo que pierden o temen, resistencia esperada, comunicación y capacitación con fecha y responsable, e incluye al grupo cuyo trabajo cambia.
- [ ] Cada fase tiene un resultado visible que comprueba alguien fuera de TI.
- [ ] Se prepararon respuestas basadas en evidencia para al menos 3 preguntas críticas probables.
- [ ] La presentación fue ensayada y cabe en el tiempo asignado (máximo 10 minutos).
- [ ] Cada integrante tiene claro qué parte presenta y puede responder preguntas sobre ella.

---

## 6. Documentos adicionales: Gobernanza y Gestión de Cambios

Estos documentos **no son un quinto acto de la charla** — el pitch se queda en 10 minutos con los 4 actos del Paso 1. Se entregan junto con el resto del paquete final como anexos que el comité puede consultar. El marco de principios y estándares (6.0) responde "con qué reglas se diseñó y se seguirá diseñando esta arquitectura"; el Plan de Implementación (Acto 4) responde "cómo ejecutamos este cambio"; los dos documentos siguientes corresponden a las fases *Implementation Governance* y *Architecture Change Management* de TOGAF ADM y responden "quién lo supervisa mientras se ejecuta" (6.2) y "qué hacemos cuando algo cambie después" (6.3).

### 6.0 Principios Arquitectónicos y Estándares

Antes de definir quién gobierna la ejecución (6.2) o cómo se gestionan cambios futuros (6.3), el comité necesita un marco de referencia explícito contra el cual validar cualquier decisión, presente o futura: los principios que orientan el diseño, los estándares tecnológicos autorizados, y un registro de las decisiones arquitectónicas más importantes ya tomadas (ADR). Sin este marco, el "Criterio de conformidad" de la sección 6.2 no tiene contra qué compararse más allá del TO-BE del Taller 7.

Defina, con base en el proyecto real del equipo:

1. **Principios Arquitectónicos** — parta del borrador de 3 principios que escribió en la Visión del Taller 0. Para cada uno diga si se **confirma**, se **reescribe** o se **retira**, con la evidencia de los Talleres 1 a 8 que lo sostiene o lo contradijo, y agregue los que el proyecto necesitó y no estaban (por ejemplo, uno de seguridad que salió del Taller 5). Mínimo 3 al final, cada uno con nombre, declaración, implicación y justificación concreta en el proyecto (no una definición de libro sin aterrizar). Un principio que se retira también se registra: el comité necesita saber qué regla dejó de aplicar y por qué.
2. **Estándares Tecnológicos** — lenguaje o framework, tipo de comunicación (REST, eventos) e infraestructura.
3. **Decisiones Arquitectónicas (ADR)** — al menos 2 decisiones importantes ya tomadas en el proyecto, llenas con Contexto, Problema, Decisión, Alternativas y Consecuencias — no una plantilla en blanco.

Los principios y estándares se entregan en `plan-gobernanza.md`; las ADR, en `procedimiento-cambios.md` (sección «Registro de decisiones»), porque ahí vive el registro que se sigue alimentando después.

**Reglas de calidad (del Módulo 8, Gobierno de Arquitectura).** El gobierno no es trámite: las reglas acotan la variabilidad y por eso permiten decidir rápido. Cada artefacto tiene una prueba concreta:

| Artefacto | Prueba de calidad | Error que el comité va a buscar |
|---|---|---|
| Principio | Redáctelo con **nombre, declaración e implicación**. Un principio bien escrito permite decir «no» a algo concreto; si no descarta ninguna opción, es una frase bonita. | Principios que no descartan ninguna opción |
| Estándar | Declare la elección **y la razón**. El estándar debe tener una puerta: las excepciones justificadas se aprueban mediante una ADR. Un catálogo cerrado sin excepciones empuja a los equipos a construir por fuera del radar. | Estándares sin razón declarada |
| ADR | Las alternativas descartadas están escritas **con su razón**. Consecuencias positivas **y** negativas (la deuda técnica que se acepta). | ADR sin alternativas descartadas; consecuencias solo positivas |

**Prueba de la escalera (governance stack).** Cada nivel restringe al de abajo: estrategia del negocio → principios → estándares → decisiones (ADR). Tome un estándar de su proyecto y suba: ¿de qué principio se desprende?, ¿y ese principio de qué objetivo de negocio? Si la cadena se rompe, el estándar sobra.

**Reglas de vida de una ADR:** se maneja por **estados** (Propuesta → Aceptada → Reemplazada por ADR-00X), nunca se edita para cambiarle el sentido y no se borra (el error también es historia); vive en el repositorio junto al código y se escribe solo para decisiones difíciles o costosas de revertir — documentar todo equivale a no documentar nada. (El módulo presenta la ADR con 4 secciones: Contexto, Alternativas, Decisión, Consecuencias; en este taller el campo *Problema* puede leerse como parte del Contexto, pero se conserva por la plantilla oficial de la entrega.)

**Cómo se llega a la decisión.** El método para decidir (marco de 8 pasos con matriz de decisión ponderada) se trabaja en el [Taller 7, sección 2.1](https://github.com/CesarAVegaF312/AREM-Taller_7_Opportunities_Solutions/blob/main/clase/guia_paso_a_paso_opportunities_solutions.md), porque ahí es donde se elige entre opciones de mejora. Aquí la ADR **registra** esa decisión: la matriz del Taller 7 aporta el Contexto, las alternativas descartadas con su razón y el trade-off aceptado.

Un *trade-off* es sacrificar conscientemente un atributo por otro más crítico (ejemplo del módulo: en un carrito de compras en Black Friday se elige alta disponibilidad y se sacrifica consistencia inmediata del inventario). Toda ADR de su entrega debería nombrar qué se sacrificó.

**Ejemplo — Principios Arquitectónicos de FarmApp:**

| Principio | Explicación | Justificación en el proyecto | Implicación (qué queda prohibido o encarecido) |
|---|---|---|---|
| API First | Toda integración entre sistemas (POS, e-commerce, pasarela de pago, logística) se expone y se consume mediante APIs versionadas y documentadas, en vez de acceso directo a bases de datos o archivos planos. | La brecha central de FarmApp (inventario desincronizado) existe porque hoy POS y e-commerce se comunican vía base de datos replicada, no vía API; este principio es la precondición de la sincronización CDC (ver ADR #1). | Queda prohibido que un sistema nuevo lea o escriba directamente en la base de datos de otro; la integración por archivos planos o réplica de tablas solo se acepta con una ADR que fije su fecha de retiro. |
| Security by Design | La autenticación, el cifrado y la gestión de consentimiento se incorporan desde el diseño de cada componente nuevo, no se agregan después como parche. | El Taller 5 (STRIDE) identificó la exposición de datos de pago como riesgo Alto (Paso 3); este principio evita que los nuevos componentes de sincronización repitan ese error. | Ningún componente nuevo pasa a producción sin su análisis STRIDE y sin cifrado en tránsito y en reposo; esto encarece y alarga cada entrega, y se acepta ese costo. |
| Cloud First / Escalabilidad | Todo componente nuevo se diseña preferentemente para la infraestructura de nube híbrida ya definida, con capacidad de escalar horizontalmente ante picos de demanda. | El Taller 4 definió la arquitectura de nube híbrida de FarmApp; este principio asegura que los componentes nuevos (gateway de integración, pipeline de CDC) la respeten en vez de crear una isla de infraestructura aparte. | Queda prohibido instalar componentes nuevos en servidores de tienda o en infraestructura fuera de la nube híbrida definida; una excepción (por ejemplo, un POS que debe operar sin conexión) exige ADR y plan de sincronización. |
| Loose Coupling | Los sistemas se comunican mediante interfaces y eventos bien definidos, evitando integraciones punto a punto fuertemente acopladas. | Sostiene técnicamente la decisión de reemplazar la base de datos replicada por eventos de cambio (ADR #1), reduciendo el riesgo de que un cambio en el POS rompa el e-commerce y viceversa. | Queda prohibido que dos sistemas compartan esquema de base de datos o llamadas síncronas encadenadas sin contrato versionado; cada integración nueva pasa por el gateway o por el bus de eventos, lo que encarece la primera integración a cambio de abaratar las siguientes. |

**Ejemplo — Estándares Tecnológicos de FarmApp:**

| Categoría | Estándar definido | Por qué |
|---|---|---|
| Lenguaje / framework | Java + Spring Boot para los nuevos microservicios de integración; el POS heredado no se reescribe (Taller 4) | Reutiliza el conocimiento del equipo de plataforma y evita el riesgo/costo de reescribir un sistema crítico en producción |
| Tipo de comunicación | REST para consultas síncronas (catálogo, disponibilidad); eventos (broker tipo Kafka/RabbitMQ) para la sincronización de inventario vía CDC | Conecta directamente con la decisión de la ADR #1: la sincronización casi en tiempo real necesita un canal de eventos, no solo peticiones síncronas |
| Infraestructura | Nube híbrida: servidores regionales on-premise para el POS heredado + nube pública para los servicios de integración y el e-commerce; balanceador de carga redundante | Continúa la decisión de nube híbrida del Taller 4 y conecta con la ADR #2 (redundancia del balanceador) |

**Ejemplo — Decisiones Arquitectónicas (ADR) de FarmApp:**

Estas 2 ADR no son hipotéticas: formalizan decisiones que ya están implícitas en el Plan de Implementación (Paso 4) de esta guía.

| Campo | ADR #1 |
|---|---|
| Título | Sincronización de inventario vía CDC en lugar de batch nocturno |
| Estado | Aceptada |
| Contexto | FarmApp sincroniza hoy el inventario entre el POS y la plataforma e-commerce mediante una base de datos replicada con corte batch (Taller 4). |
| Problema | El retraso de varias horas entre corte y corte hace que el e-commerce muestre disponibilidad que ya no existe en tienda, generando pedidos que no se pueden despachar (riesgo "Retraso de sincronización de inventario", Paso 3, prioridad 1). |
| Decisión | Reemplazar el batch nocturno por sincronización casi en tiempo real usando Change Data Capture (CDC) sobre la base del POS, publicando los cambios de inventario como eventos que consume el e-commerce. |
| Alternativas consideradas | (a) Aumentar la frecuencia del batch (ej. cada 15 min): no elimina el riesgo en horas pico, solo lo reduce. (b) Reescribir el POS heredado para escritura compartida: alto costo y riesgo de romper un sistema crítico en producción. (c) CDC: menor intrusión sobre el sistema heredado y coherente con los principios API First y Loose Coupling. |
| Consecuencias | (+) El e-commerce refleja el inventario real en segundos y deja de vender lo que no hay. (−) Se acepta un componente crítico nuevo que operar y monitorear (el bus de eventos y el pipeline de CDC) y consistencia eventual de algunos segundos entre POS y e-commerce. **Trade-off aceptado:** se sacrifica simplicidad operativa a cambio de consistencia casi en tiempo real. Corresponde a la fase "Mediano plazo" del Plan de Implementación (Paso 4), esfuerzo Alto, responsable Plataforma. |

| Campo | ADR #2 |
|---|---|
| Título | Balanceador de carga redundante activo-pasivo en lugar de activo-activo |
| Estado | Aceptada |
| Contexto | El Taller 4 identificó un balanceador de carga único como punto único de falla (SPOF) para la disponibilidad de la plataforma e-commerce (riesgo "Punto único de falla en el balanceador de carga", Paso 3, prioridad 3). |
| Problema | Ante la caída del balanceador activo, toda la operación digital de FarmApp queda inaccesible, sin mecanismo de contingencia. |
| Decisión | Implementar un segundo balanceador en configuración activo-pasivo con failover automático, en vez de una configuración activo-activo. |
| Alternativas consideradas | (a) Activo-activo: descartada en esta fase por exigir sincronización de sesión y mayor complejidad operacional frente a un beneficio marginal dado el volumen actual de tráfico. (b) Mantener un único balanceador con monitoreo reforzado: no elimina el SPOF, solo acorta el tiempo de detección. (c) Activo-pasivo: menor complejidad y costo, adecuada al volumen de tráfico actual. |
| Consecuencias | Se acepta un tiempo de failover no-cero (RTO) en vez de conmutación instantánea; la decisión puede revisarse en la Revisión periódica completa (sección 6.3) si se activa el disparador de crecimiento de demanda (+30% pedidos mensuales); corresponde a la fase "Largo plazo" del Plan de Implementación (Paso 4), esfuerzo Medio, responsable Infraestructura. |

### 6.2 Plan de Gobernanza de la Implementación

Defina, en 4 puntos:

1. **Mecanismo de gobierno** — quién revisa el avance del roadmap (Acto 4) y con qué frecuencia.
2. **Criterio de conformidad** — cómo se verifica que cada fase implementada respeta el diseño aprobado en el Taller 7 (Opportunities & Solutions).
3. **Escalamiento** — qué pasa si una fase necesita desviarse del diseño aprobado (quién autoriza la excepción).
4. **Cadencia de seguimiento** — cada cuánto se reporta el avance del roadmap.

**Ejemplo — FarmApp:**

| Elemento | Definición |
|---|---|
| Comité de Arquitectura | Arquitecto líder + representante de negocio + representante de seguridad |
| Cadencia | Reunión mensual mientras dure la ejecución del roadmap (Taller 9, Paso 4) |
| Criterio de conformidad | Una fase se cierra solo si el arquitecto líder valida que el resultado coincide con el TO-BE del Taller 7 |
| Escalamiento | Cualquier desviación del diseño aprobado (ej. por restricción de presupuesto) requiere aprobación escrita del comité antes de continuar |

#### 6.2.1 Métricas de gobierno: cómo saber si el gobierno funciona

Un comité que se reúne cada mes no prueba que el gobierno funcione. Defina **3 métricas**, cada una con estos 5 campos — sin fórmula no se calcula y sin umbral no avisa:

1. **Qué mide**: atada a uno de los principios de la sección 6.0 (¿se está cumpliendo de verdad?).
2. **Fórmula**: algo que se puede calcular, no "mejorar la integración".
3. **Fuente que ya existe hoy**: un inventario, un registro o un sistema que el cliente ya tiene. Si la métrica necesita un sistema que no existe, todavía no se puede calcular: es un deseo con forma de fórmula.
4. **Línea base**: el valor de hoy, calculado con los datos del AS-IS de los talleres anteriores.
5. **Umbral**: el valor a partir del cual el comité debe actuar.

**Una de las tres debe medir al propio comité.** El mayor riesgo de un sistema de gobierno es que estorbe: si el comité tarda más que el plazo del negocio, los equipos empiezan a construir por fuera de él.

**Ejemplo — FarmApp:**

| Métrica | Qué mide (principio) | Fórmula | Fuente que ya existe | Línea base | Umbral |
|---|---|---|---|---|---|
| M1 · Integraciones por API | Si se cumple **API First** | Integraciones expuestas por API versionada ÷ integraciones totales × 100 | Inventario de integraciones del tablero integrado (Taller 8; en un cliente real, también el C2 del Taller 3) | 2 de 5 = 40%: por API, e-commerce ↔ pasarela de pagos y e-commerce ↔ CRM; sin API, POS ↔ e-commerce e inventario ↔ e-commerce (BD replicada) y e-commerce ↔ logística (archivo plano) | No sube al menos 20 puntos en el semestre siguiente |
| M2 · Flujo de pagos cifrado | Si se cumple **Security by Design** | Conexiones del flujo de pagos con TLS ÷ conexiones totales del flujo × 100 | Tabla STRIDE del flujo de pagos (en un cliente real, Taller 5) | 3 de 5 = 60% | Cualquier valor menor a 100% al cerrar la fase Corto plazo |
| M3 · Tiempo de dictamen del comité | Si el **gobierno** estorba | Días hábiles entre la propuesta de una ADR o excepción y su dictamen | Registro de ADR del procedimiento de cambios (fechas Propuesta → Aceptada) | Se mide desde la primera solicitud | Más de 10 días hábiles |

> M3 no tiene línea base porque el registro de ADR empieza a existir con este plan — dígalo así, no invente un valor. M1 y M2 sí la tienen, porque salen de vistas que el equipo ya construyó.

### 6.3 Procedimiento de Actualización y Revisión de la Arquitectura

A diferencia del Plan de Implementación (que ejecuta un cambio ya decidido), este procedimiento cubre qué pasa **después**, cuando el roadmap ya se ejecutó y surge la necesidad de un cambio nuevo. Defina:

1. **Disparadores de cambio** — qué eventos ameritan revisar la arquitectura (nueva regulación, cambio de proveedor, incidente de seguridad, crecimiento inesperado de demanda).
2. **Proceso de cambio** — quién propone un cambio, quién lo evalúa y en cuánto tiempo.
3. **Registro de decisiones** — use un ADR (Architecture Decision Record) simple para dejar constancia de cada decisión.
4. **Revisión periódica completa** — cada cuánto se revisa toda la arquitectura contra el estado real del negocio (no solo ante un disparador puntual).

**Ejemplo — FarmApp:**

| Disparador de cambio | Ejemplo concreto |
|---|---|
| Nueva regulación | Cambio en la Ley 1581 sobre datos de salud (medicamentos con prescripción) |
| Cambio de proveedor | Migración del proveedor de nube actual, o del proveedor único de logística (riesgo de Negocio identificado en el Paso 3) |
| Incidente de seguridad | Una brecha real en el flujo de pagos |
| Crecimiento de demanda | Aumento de +30% en pedidos mensuales |

**Plantilla mínima de ADR** (para registrar decisiones futuras; los 2 ADR ya resueltos del proyecto están en la sección 6.0):

| Campo | Contenido |
|---|---|
| Título | Nombre corto de la decisión |
| Estado | Propuesta / Aceptada / Reemplazada |
| Fecha de propuesta | Cuándo se pidió la decisión (alimenta la métrica M3) |
| Fecha de dictamen | Cuándo la aceptó o rechazó el comité |
| Contexto | Qué disparó la necesidad de decidir |
| Problema | Qué problema concreto genera no decidir, o decidir mal |
| Decisión | Qué se decidió |
| Alternativas consideradas | Qué otras opciones se evaluaron y por qué no se eligieron |
| Consecuencias | Qué se gana (+), qué se pierde o qué deuda se acepta (−), y el trade-off aceptado |

**Checklist de estos tres documentos:**

- [ ] Están definidos al menos 3 principios arquitectónicos, cada uno explicado y justificado en el proyecto (no genéricos de manual).
- [ ] Los 3 estándares (lenguaje/framework, comunicación, infraestructura) tienen elecciones concretas para el proyecto, no solo la categoría.
- [ ] Existen al menos 2 ADR reales y llenos (Contexto, Problema, Decisión, Alternativas, Consecuencias), no una plantilla en blanco.
- [ ] Cada principio permite decir «no» a algo concreto, y cada estándar declara su razón.
- [ ] Cada ADR incluye las alternativas descartadas con su razón y consecuencias negativas (no solo positivas), y nombra el trade-off aceptado.
- [ ] Cada estándar se puede rastrear hacia arriba: estándar → principio → objetivo de negocio.
- [ ] El plan de gobernanza define quién revisa la implementación y con qué frecuencia.
- [ ] El criterio de conformidad está trazado al TO-BE del Taller 7, no es una opinión subjetiva.
- [ ] Hay 3 métricas de gobierno, cada una con qué mide (principio), fórmula, fuente que ya existe, línea base y umbral, y una de ellas mide al propio comité (sección 6.2.1).
- [ ] El procedimiento de cambios define disparadores concretos, no solo "cuando sea necesario".
- [ ] Existe un formato de ADR (o equivalente) para registrar decisiones futuras.
- [ ] Está definida una cadencia de revisión periódica completa de la arquitectura.

---

## 7. Vistas ArchiMate (obligatorias en la entrega final)

La entrega final incluye **dos vistas ArchiMate** en `entrega/vistas-finales/`: la de **Implementación y Migración** (7.1) y la de **Motivación** (7.2). Pueden construirse en Archi o en draw.io con la biblioteca "ArchiMate 3"; en ambos casos se entrega también una imagen PNG. No se presentan necesariamente en los 10 minutos: son anexos que el panel puede consultar.

### 7.1 Vista de Implementación y Migración

Cierra la cadena que empezó en el Taller 7: cada fase del Plan de Implementación (Paso 4) es un **Work Package** de la capa de Implementación y Migración (ver la [Guía de Notación ArchiMate](https://github.com/CesarAVegaF312/AREM-ArchiMate/blob/main/guia_notacion_archimate.md)) asociado al Gap que resuelve, y que **realiza** el nuevo Plateau TO-BE. En ArchiMate el Gap solo se **asocia**: con los dos Plateaus que separa y con el Work Package que lo cierra.

```mermaid
flowchart LR
    asis["Plateau: FarmApp AS-IS"]
    gap(["Gap: sincronización de inventario"])
    wp["Work Package: Sincronización CDC POS-Ecommerce"]
    tobe["Plateau: FarmApp TO-BE"]

    asis ---|"asociación"| gap
    gap ---|"asociación"| tobe
    wp ---|"cierra (asociación)"| gap
    wp -.->|"realiza"| tobe

    classDef migracion fill:#ffcc99,color:#000,stroke:#cc6600;
    class asis,gap,wp,tobe migracion
```

Los Principios Arquitectónicos (sección 6.0) también tienen su lugar en ArchiMate: son los `Principle` que restringen y orientan cada `Work Package`, y las ADR resueltas documentan por qué se eligió una realización concreta del Gap y no otra. El Plan de Gobernanza (sección 6.2) y el Procedimiento de Cambios (sección 6.3) también tienen su lugar en ArchiMate: el primero define quién valida que cada `Work Package` efectivamente produce el `Plateau` esperado; el segundo describe el proceso para, más adelante, abrir un nuevo ciclo Constraint/Requirement → Gap → Work Package cuando surja una necesidad de cambio no prevista en este semestre.

En la vista del cliente real debe aparecer **una fila del plan de implementación = un Work Package**, cada uno asociado al Gap de la matriz de brechas del Taller 7 que cierra, y todos realizando el Plateau TO-BE (opcionalmente, Plateaus intermedios si una fase deja la arquitectura en un estado estable propio).

### 7.2 Vista de Motivación

Muestra el «porqué» de toda la propuesta, en la misma escalera de la sección 6.0 (estrategia → principios → estándares → decisiones):

```mermaid
flowchart LR
    driver(["Driver: inventario desincronizado genera pedidos fallidos"])
    goal(["Goal: no perder ventas por falta de stock real"])
    principle(["Principle: API First"])
    req(["Requirement: sincronización de inventario casi en tiempo real"])
    wp["Work Package: Sincronización CDC POS-Ecommerce"]

    driver -.->|"influye en"| goal
    principle -->|"realiza"| goal
    req -->|"realiza"| principle
    req -->|"realiza"| goal
    wp -->|"realiza"| req

    classDef motivacion fill:#ccccff,color:#000,stroke:#6666cc;
    classDef migracion fill:#ffcc99,color:#000,stroke:#cc6600;
    class driver,goal,principle,req motivacion
    class wp migracion
```

En la vista del cliente real: los `Driver` y `Goal` salen de los problemas y objetivos estratégicos de la Ficha de Caracterización (Taller 0); los `Principle` son los de la sección 6.0; los `Requirement` y `Constraint` salen de las brechas de los Talleres 5-7. Cada `Goal` debe quedar realizado por al menos un `Requirement`, y cada `Requirement` por al menos un `Work Package` de la vista 7.1 — un objetivo del cliente sin nada que lo realice es justo la pregunta que el panel va a hacer.

**Checklist de las vistas ArchiMate:**

- [ ] Existen las dos vistas (Motivación y Migración) en `entrega/vistas-finales/`, con su PNG.
- [ ] Cada fase del plan de implementación aparece como un Work Package que resuelve un Gap del Taller 7.
- [ ] Cada Goal del cliente (Ficha, Taller 0) está realizado por al menos un Requirement, y cada Requirement por un Work Package.
- [ ] Los Principles de la vista son los mismos del plan de gobernanza (sección 6.0).
- [ ] Se usan los elementos y relaciones de la [Guía de Notación ArchiMate](https://github.com/CesarAVegaF312/AREM-ArchiMate/blob/main/guia_notacion_archimate.md), con el color de cada capa.

---

_Esta guía hace parte del Taller 9 de Simulación de Comité de Arquitectura — curso Arquitectura Empresarial, Universidad de La Sabana._
