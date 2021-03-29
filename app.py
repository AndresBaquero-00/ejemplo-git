from flask import Flask, render_template, request
from calculadora import Calculadora

app = Flask('Calculadora')

@app.route('/')
def main():
    return render_template('index.html')

#@app.route('/suma/<int:valor_1>/<int:valor_2>')
def suma(valor_1: int, valor_2: int):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.sumar()

    return str(c.resultado)

#@app.route('/resta/<int:valor_1>/<int:valor_2>')
def resta(valor_1: int, valor_2: int):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.restar()

    return str(c.resultado)

#@app.route('/multiplicacion/<int:valor_1>/<int:valor_2>')
def multiplicacion(valor_1: int, valor_2: int):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.multiplicar()

    return str(c.resultado)

#@app.route('/division/<int:valor_1>/<int:valor_2>')
def division(valor_1: int, valor_2: int):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.dividir()

    return str(c.resultado)

@app.route('/operacion', methods = ['GET', 'POST'])
def operacion():
    operador = request.args.get('operador', type = str)
    valor_1 = request.args.get('valor_1', type = float)
    valor_2 = request.args.get('valor_2', type = float)
    resultado = None
    if operador == 'suma':
        resultado = suma(valor_1, valor_2)
    elif operador == 'resta':
        resultado = resta(valor_1, valor_2)
    elif operador == 'multiplicacion':
        resultado = multiplicacion(valor_1, valor_2)
    elif operador == 'division':
        resultado = division(valor_1, valor_2)
    else:
        resultado = 0

    return render_template('index.html', resultado = resultado)

if __name__ == '__main__':
    app.run(debug = True)