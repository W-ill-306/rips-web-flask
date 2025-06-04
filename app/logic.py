
import sqlite3
import json
from datetime import datetime

DB_PATH = "rips.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def cargar_opciones(tabla, col_codigo="codigo", col_nombre=None, codigos_permitidos=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({tabla})")
        columnas = [col[1].lower() for col in cursor.fetchall()]

        if not col_nombre:
            if 'descripcion' in columnas:
                col_nombre = 'descripcion'
            elif 'nombre' in columnas:
                col_nombre = 'nombre'
            else:
                raise Exception("No se encontró columna válida para nombre")

        cursor.execute(f"SELECT {col_codigo}, {col_nombre} FROM {tabla}")
        resultados = cursor.fetchall()

        if codigos_permitidos:
            resultados = [(str(c), n) for c, n in resultados if str(c) in codigos_permitidos]

        opciones = [{"codigo": str(c), "nombre": n} for c, n in resultados]
        return opciones
    except Exception as e:
        print(f"Error cargando {tabla}: {e}")
        return []

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def generar_json(data):
    # Estructura base con campos principales
    estructura = {
        "numDocumentoIdObligado": data.get("numDocumentoIdObligado", ""),
        "numFactura": data.get("numFactura", ""),
        "tipoNota": None if data.get("tipoNota") == "null" else data.get("tipoNota"),
        "numNota": None if data.get("tipoNota") == "null" else data.get("numNota"),
        "codPrestador": data.get("codPrestador", ""),
        "usuarios": []
    }

    # Estructura de usuario
    usuario = {
        "tipoDocumentoIdentificacion": data.get("tipoDocumentoIdentificacion", ""),
        "numDocumentoIdentificacion": data.get("numDocumentoIdentificacion", ""),
        "codSexo": data.get("codSexo", ""),
        "fechaNacimiento": data.get("fechaNacimiento", ""),
        "servicios": {
            "consultas": []
        }
    }

    consulta = {
        "codPrestador": estructura["codPrestador"],
        "numFactura": estructura["numFactura"],
        "fechaInicioAtencion": data.get("fechaInicioAtencion"),
        "codConsulta": data.get("codConsulta"),
        "vrServicio": data.get("vrServicio")
    }

    usuario["servicios"]["consultas"].append(consulta)
    estructura["usuarios"].append(usuario)

    return estructura
