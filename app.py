from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    mensaje = "<h1> !Hola bienvenido a la calculadora de Flask!</h1>"
    
    mensaje += "<h2>Para poder usarla tendras que hacer</h2>"
    mensaje += "<ol>"
    mensaje += "<li><h2>Sumar http://127.0.0.1:5000/sumar/10/20</h2></li>"
    mensaje += "<li><h2>Restar http://127.0.0.1:5000/restar/10/20</h2></li>"
    mensaje += "<li><h2>Dividir http://127.0.0.1:5000/dividir/10/20</h2></li>"
    mensaje += "<li><h2>Multiplicar http://127.0.0.1:5000/multiplicar/10/20</h2></li>"
    mensaje += "<li><h2>Maximo http://127.0.0.1:5000/maximo/10/20</h2></li>"
    mensaje += "<li><h2>Minimo http://127.0.0.1:5000/minimo/10/20</h2></li>"
    mensaje += "</ol>"
    return mensaje

@app.route("/sumar/<v1>/<v2>")
def sumar(v1,v2):
    s = str(float(v1) + float(v2))
    mensaje = f"<h1>La Suma de {v1} + {v2} es {s} </h1>"
    return mensaje

@app.route("/restar/<v1>/<v2>")
def restar(v1,v2):
    s = str(float(v1) + float(v2))
    mensaje = f"<h1>La Resta de {v1} - {v2} es {s}</h1>"
    return mensaje

@app.route("/dividir/<v1>/<v2>")
def dividir(v1,v2):
    s = str(float(v1) / float(v2))
    mensaje = f"<h1>La division de {v1} entre {v2} da como resultado {s}"
    return mensaje

@app.route("/multiplicar/<v1>/<v2>")
def mulriplicar(v1,v2):
    s = str(float(v1) * float(v2))
    mensaje = f"<h1>La multiplicacion de {v1} entre {v2} da como resultado {s}"
    return mensaje

@app.route("/maximo/<v1>/<v2>")
def maximo(v1,v2):
    if v1>v2:
        mensaje1 = f"<h1>El numero mayo es {v1}"
        return mensaje1
    else:
        mensaje = f"<h1>El numero mayor es {v2}"
        return mensaje
    
@app.route("/minimo/<v1>/<v2>")
def minimo(v1,v2):
    if v1<v2:
        mensaje = f"<h1>El numero menor es {v1}"
        return mensaje
    else:
        mensaje = f"<h1>El numero menor es {v2}"
        return mensaje

if __name__ == "__main__":
    app.run(debug=True)