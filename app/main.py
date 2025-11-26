from flask import Flask, jsonify, render_template, request

def create_app():
    app = Flask(__name__)

    # Interfaz gráfica
    @app.get("/")
    def home():
        return render_template("calculadora.html")

    @app.post("/calcular")
    def calcular():
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["op"]

            if op == "suma":
                resultado = a + b
            elif op == "resta":
                resultado = a - b
            elif op == "mul":
                resultado = a * b
            elif op == "div":
                if b == 0:
                    return render_template("calculadora.html", error="No se puede dividir por cero")
                resultado = a / b
            else:
                return render_template("calculadora.html", error="Operación no válida")

            return render_template("calculadora.html", resultado=resultado)

        except Exception:
            return render_template("calculadora.html", error="Datos inválidos")

    # Endpoints API JSON
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
