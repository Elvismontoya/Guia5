from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify({"mensaje": "API Calculadora Lista", "operaciones": ["suma", "resta", "mul", "div"]})

    @app.get("/suma/<int:a>/<int:b>")
    def suma(a, b):
        return jsonify({"resultado": a + b})

    @app.get("/resta/<int:a>/<int:b>")
    def resta(a, b):
        return jsonify({"resultado": a - b})

    @app.get("/mul/<int:a>/<int:b>")
    def multiplicacion(a, b):
        return jsonify({"resultado": a * b})

    @app.get("/div/<int:a>/<int:b>")
    def division(a, b):
        if b == 0:
            return jsonify({"error": "No se puede dividir por cero"}), 400
        return jsonify({"resultado": a / b})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)

    