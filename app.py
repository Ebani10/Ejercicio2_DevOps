from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def log_change(action):
    with open("backup.log", "a+") as f:
        f.write(f"[{datetime.datetime.now()}] - {action}\n")
        f.flush()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        calc_type = request.form.get("type")
        try:
            if calc_type == "arithmetic":
                expr = request.form.get("expression")
                result = eval(expr) # Nota: Solo para fines académicos
            elif calc_type == "binary":
                num = int(request.form.get("num"))
                result = bin(num)
            # Sección lógica (Punto 8)
            elif calc_type == "logic":
                val1 = request.form.get("val1") == 'True'
                val2 = request.form.get("val2") == 'True'
                op = request.form.get("op")
                result = (val1 and val2) if op == 'AND' else (val1 or val2)
                
            log_change(f"Calculadora {calc_type} utilizada. Resultado: {result}")
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)