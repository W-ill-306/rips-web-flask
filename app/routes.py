from flask import Flask, render_template, request, send_file
from app.logic import generar_json, obtener_datos_formulario
import io
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        datos = obtener_datos_formulario(request.form)
        json_data = generar_json(datos)
        return render_template("preview.html", json_pretty=json.dumps(json_data, indent=4, ensure_ascii=False))

    return render_template("index.html")

@app.route("/descargar", methods=["POST"])
def descargar():
    datos = obtener_datos_formulario(request.form)
    json_data = generar_json(datos)

    buffer = io.BytesIO()
    buffer.write(json.dumps(json_data, indent=4, ensure_ascii=False).encode("utf-8"))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="salida_rips.json", mimetype="application/json")
