# Guia5
# Realizado por: Elvis Alberto Montoya Rondón
# Python 12 maximo instalado

Proyecto para la guia5: una API que realiza:

- Suma http://127.0.0.1:5000/suma/10/5
- Resta http://127.0.0.1:5000/resta/10/5
- Multiplicación http://127.0.0.1:5000/mul/10/5
- División http://127.0.0.1:5000/div/10/5
- División por 0 devuelve error http://127.0.0.1:5000/div/10/0

Incluye pruebas automatizadas con **pytest** y CI/CD con GitHub Actions.

## 🚀 Ejecutar localmente
Rquiere Version
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
python app/main.py