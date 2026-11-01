# Procedimiento de Actualización y Revisión de la Arquitectura — FarmApp (ejemplo)

Archivo de ejemplo para probar `verificar_gobierno.py`. Solo contiene la sección «Registro de decisiones»: las ADR #1 y #2 son las de la sección 6.0 de la guía, con fechas inventadas para el ejemplo, y la ADR #3 es una decisión que el comité todavía no ha dictaminado.

## Registro de decisiones (ADR)

| Campo | ADR #1 |
|---|---|
| Título | Sincronización de inventario vía CDC en lugar de batch nocturno |
| Estado | Aceptada |
| Fecha de propuesta | 05/10/2026 |
| Fecha de dictamen | 09/10/2026 |
| Contexto | FarmApp sincroniza hoy el inventario entre el POS y la plataforma e-commerce mediante una base de datos replicada con corte batch (Taller 4). |
| Problema | El retraso de varias horas entre corte y corte hace que el e-commerce muestre disponibilidad que ya no existe en tienda. |
| Decisión | Reemplazar el batch nocturno por sincronización casi en tiempo real usando Change Data Capture (CDC) sobre la base del POS. |
| Alternativas consideradas | (a) Aumentar la frecuencia del batch: no elimina el riesgo en horas pico. (b) Reescribir el POS heredado: alto costo y riesgo. (c) CDC: menor intrusión y coherente con API First y Loose Coupling. |
| Consecuencias | (+) El e-commerce refleja el inventario real en segundos. (−) Se acepta un componente crítico nuevo que operar y consistencia eventual de algunos segundos. Trade-off: simplicidad operativa a cambio de consistencia casi en tiempo real. |

| Campo | ADR #2 |
|---|---|
| Título | Balanceador de carga redundante activo-pasivo en lugar de activo-activo |
| Estado | Aceptada |
| Fecha de propuesta | 13/10/2026 |
| Fecha de dictamen | 30/10/2026 |
| Contexto | El Taller 4 identificó un balanceador de carga único como punto único de falla. |
| Problema | Ante la caída del balanceador activo, toda la operación digital de FarmApp queda inaccesible. |
| Decisión | Implementar un segundo balanceador en configuración activo-pasivo con failover automático. |
| Alternativas consideradas | (a) Activo-activo: más complejidad sin beneficio claro con el tráfico actual. (b) Un solo balanceador con monitoreo reforzado: no elimina el punto único de falla. (c) Activo-pasivo: menor complejidad y costo. |
| Consecuencias | (+) Se elimina el punto único de falla. (−) Se acepta un tiempo de failover distinto de cero. Trade-off: conmutación instantánea a cambio de menor complejidad. |

| Campo | ADR #3 |
|---|---|
| Título | Despliegue escalonado de las actualizaciones del POS por grupos de tiendas |
| Estado | Propuesta |
| Fecha de propuesta | 26/10/2026 |
| Fecha de dictamen | |
| Contexto | Hoy las actualizaciones del POS se instalan en todas las tiendas la misma noche. |
| Problema | Una actualización defectuosa detiene las ventas de todas las tiendas a la vez. |
| Decisión | Instalar cada actualización primero en 2 tiendas piloto, esperar 48 horas y luego extenderla al resto por grupos. |
| Alternativas consideradas | (a) Mantener la instalación simultánea: más rápida, pero sin forma de contener una falla. (b) Probar solo en un ambiente de pruebas: no reproduce las condiciones reales de cada tienda. |
| Consecuencias | (+) Una falla queda contenida en las tiendas piloto. (−) Una corrección urgente tarda más en llegar a todas las tiendas. Trade-off: velocidad de despliegue a cambio de contención del riesgo. |
