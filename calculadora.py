''' Clase para realizar operaciones básicas '''
class Calculadora:
    def __init__(self):
        self.valor_1 = 0
        self.valor_2 = 0
        self.resultado = 0
    ''' Operación suma '''
    def sumar(self) -> None:
        self.resultado = self.valor_1 + self.valor_2
    ''' Operación resta '''
    def restar(self) -> None:
        self.resultado = self.valor_1 - self.valor_2
    ''' Operación multiplicación '''
    def multiplicar(self) -> None:
        self.resultado = self.valor_1 * self.valor_2
    ''' Operación división '''
    def dividir(self) -> None:
        self.resultado = self.valor_1 / self.valor_2

