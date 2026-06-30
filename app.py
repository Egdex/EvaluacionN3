from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "La app funciona correctamente"

@app.route("/Hola")
def saludo():
    usuario = request.args.get("usuario", "Invitado")
    return {
        "mensaje": f"Holi {usuario}",
        "estado": "ok"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)