def obtener_datos_formulario(form):
    return {
        "numDocumentoIdObligado": form.get("numDocumentoIdObligado"),
        "numFactura": form.get("numFactura"),
        "codPrestador": form.get("codPrestador"),
        "usuarios": [{
            "tipoDocumentoIdentificacion": form.get("tipoDocumentoIdentificacion"),
            "numDocumentoIdentificacion": form.get("numDocumentoIdentificacion"),
            "codSexo": form.get("codSexo"),
            "fechaNacimiento": form.get("fechaNacimiento"),
            "servicios": {
                "consultas": [{
                    "codPrestador": form.get("codPrestador"),
                    "numFactura": form.get("numFactura"),
                    "fechaInicioAtencion": form.get("fechaInicioAtencion"),
                    "codConsulta": form.get("codConsulta"),
                    "vrServicio": form.get("vrServicio")
                }]
            }
        }]
    }

def generar_json(data):
    return data
