from flask import Flask
import math
app = Flask(__name__)

@app.route('/')
def index():
    return "Calculadora con parametros"

@app.route('/suma/<int:n1>/<int:n2>')
def suma(n1, n2):
    return "El resultado de la suma es: {}" .format(n1 + n2)

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1, n2):
    return "El resultado de la resta es: {}" .format(n1 - n2)

@app.route('/multiplicacion/<int:n1>/<int:n2>')
def multiplicacion(n1, n2):
    return "El resultado de la suma es: {}" .format(n1 * n2)

@app.route('/division/<int:n1>/<int:n2>')
def division(n1, n2):
    return "El resultado de la resta es: {}" .format(n1 / n2)

@app.route('/potencia/<int:n1>/<int:n2>')
def potencia(n1,n2):
    return "El resultado de la potencia es: {}" .format(n1 ** n2)

@app.route('/raiz/<int:n1>')
def raiz(n1):
    return "El resultado de la raiz cuadrada es: {}" .format(math.sqrt(n1))

if __name__ == '__main__':
    app.run(port = 8000, debug = True)
