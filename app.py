from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "<h1>¡Hola Juan!</h1>"

@app.route("/nombre")
def hola_mundo2():
    return "<h1>¡Hola Roberto y Juan!</h1>"

if __name__ == "__main__":
    app.run(debug=True)