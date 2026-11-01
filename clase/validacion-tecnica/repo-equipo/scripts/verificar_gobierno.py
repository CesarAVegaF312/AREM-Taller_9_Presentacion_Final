#!/usr/bin/env python3
"""Verificaciones de gobierno de arquitectura para el repositorio del equipo (Taller 9).

Uso:
    python3 scripts/verificar_gobierno.py adr 09-presentacion-final/procedimiento-cambios.md
    python3 scripts/verificar_gobierno.py pr origin/main

- "adr" revisa que cada ADR del registro de decisiones esté completa (las reglas de
  calidad de la sección 6.0 de la guía) y calcula la métrica M3: días hábiles entre la
  propuesta y el dictamen del comité.
- "pr" revisa que un cambio a la arquitectura objetivo o al gobierno venga con su ADR,
  es decir, que el mismo cambio también modifique el registro de decisiones.

No necesita instalar nada: solo Python 3.
"""
import re
import subprocess
import sys
from datetime import date, datetime, timedelta

# Archivos y carpetas cuyo cambio es un cambio de arquitectura (ajústelos a su proyecto).
RUTAS_ARQUITECTURA = [
    "07-opportunities-solutions/to-be-",
    "09-presentacion-final/vistas-finales/",
    "09-presentacion-final/plan-gobernanza.md",
]
# Dónde vive el registro de decisiones (sección «Registro de decisiones» de la plantilla).
REGISTRO = "09-presentacion-final/procedimiento-cambios.md"

CAMPOS = [
    "Título", "Estado", "Fecha de propuesta", "Fecha de dictamen", "Contexto",
    "Problema", "Decisión", "Alternativas consideradas", "Consecuencias",
]
ESTADO_VALIDO = re.compile(r"^(Propuesta|Aceptada|Rechazada|Reemplazada( por ADR.*)?)$")
UMBRAL_DIAS = 10  # Umbral de la métrica M3 del ejemplo de FarmApp (sección 6.2.1).


def leer_adrs(texto):
    """Devuelve una lista de (nombre, {campo: valor}) por cada tabla «| Campo | ADR ... |»."""
    adrs, actual = [], None
    for linea in texto.splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if linea.strip().startswith("|") and len(celdas) >= 2:
            if celdas[0] == "Campo" and celdas[1].startswith("ADR"):
                actual = (celdas[1], {})
                adrs.append(actual)
            elif actual and not set(celdas[0]) <= set("-: "):
                actual[1][celdas[0]] = "|".join(celdas[1:]).strip()
        else:
            actual = None
    return adrs


def leer_fecha(valor):
    for formato in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(valor, formato).date()
        except ValueError:
            pass
    return None


def dias_habiles(desde, hasta):
    """Días de lunes a viernes después de «desde» y hasta «hasta» (no descuenta festivos)."""
    dias, d = 0, desde
    while d < hasta:
        d += timedelta(days=1)
        if d.weekday() < 5:
            dias += 1
    return dias


def revisar_adr(ruta, hoy=None):
    hoy = hoy or date.today()
    try:
        texto = open(ruta, encoding="utf-8").read()
    except FileNotFoundError:
        print(f"{ruta} todavía no existe: no hay registro de decisiones que revisar.")
        return 0
    adrs = leer_adrs(texto)
    if not adrs:
        print(f"ERROR: {ruta} no tiene ninguna tabla «| Campo | ADR #n |».")
        return 1
    errores = 0
    print(f"Registro de decisiones: {ruta} ({len(adrs)} ADR)\n")
    for nombre, campos in adrs:
        problemas = []
        estado = campos.get("Estado", "")
        for campo in CAMPOS:
            # Una ADR en estado Propuesta todavía no tiene dictamen.
            if campo == "Fecha de dictamen" and estado == "Propuesta":
                continue
            if not campos.get(campo):
                problemas.append(f"falta «{campo}»")
        if estado and not ESTADO_VALIDO.match(estado):
            problemas.append(f"el estado «{estado}» no es Propuesta, Aceptada, Rechazada ni Reemplazada")
        alternativas = campos.get("Alternativas consideradas", "")
        if alternativas.startswith("(con la razón"):
            problemas.append("las alternativas consideradas siguen con el texto de la plantilla")
        consecuencias = campos.get("Consecuencias", "")
        if "qué se gana" in consecuencias:
            problemas.append("las consecuencias siguen con el texto de la plantilla")
        elif consecuencias and "(−)" not in consecuencias and "(-)" not in consecuencias:
            problemas.append("las consecuencias no declaran nada negativo (−): toda ADR acepta algún costo")

        propuesta = leer_fecha(campos.get("Fecha de propuesta", ""))
        dictamen = leer_fecha(campos.get("Fecha de dictamen", ""))
        m3 = ""
        if campos.get("Fecha de propuesta") and not propuesta:
            problemas.append("la fecha de propuesta no tiene formato DD/MM/AAAA")
        if campos.get("Fecha de dictamen") and not dictamen and estado != "Propuesta":
            problemas.append("la fecha de dictamen no tiene formato DD/MM/AAAA")
        if propuesta and dictamen:
            if dictamen < propuesta:
                problemas.append("el dictamen es anterior a la propuesta")
            else:
                dias = dias_habiles(propuesta, dictamen)
                m3 = f"M3 = {dias} días hábiles"
                if dias > UMBRAL_DIAS:
                    m3 += f" (supera el umbral de {UMBRAL_DIAS}: el comité debe revisar su proceso)"
        elif propuesta and estado == "Propuesta":
            dias = dias_habiles(propuesta, hoy)
            m3 = f"en espera de dictamen hace {dias} días hábiles"
            if dias > UMBRAL_DIAS:
                m3 += f" (supera el umbral de {UMBRAL_DIAS})"

        titulo = campos.get("Título") or "(sin título)"
        if problemas:
            errores += 1
            print(f"[REVISAR] {nombre}: {titulo}")
            for p in problemas:
                print(f"    - {p}")
        else:
            print(f"[OK] {nombre}: {titulo} · {estado} · {m3}")
    print()
    if errores:
        print(f"{errores} ADR no cumplen las reglas de calidad de la sección 6.0 de la guía.")
        return 1
    print("Todas las ADR cumplen las reglas de calidad.")
    return 0


def revisar_pr(base):
    cambiados = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    de_arquitectura = [a for a in cambiados if any(a.startswith(r) for r in RUTAS_ARQUITECTURA)]
    if not de_arquitectura:
        print("Este cambio no toca la arquitectura objetivo ni el gobierno: no necesita ADR.")
        return 0
    print("Este cambio toca la arquitectura:")
    for a in de_arquitectura:
        print(f"    - {a}")
    if REGISTRO in cambiados:
        print(f"\nTrae su ADR: también modifica {REGISTRO}.")
        return 0
    print(f"\nERROR: no modifica {REGISTRO}. Registre la decisión como una ADR antes de pedir la revisión.")
    return 1


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "adr":
        sys.exit(revisar_adr(sys.argv[2]))
    if len(sys.argv) == 3 and sys.argv[1] == "pr":
        sys.exit(revisar_pr(sys.argv[2]))
    print(__doc__)
    sys.exit(2)
