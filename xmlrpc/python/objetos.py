class Calculadora(object):
    def __init__(self):
        self.operacoes = {'soma':self.soma,'subtracao':self.subtracao}

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a-b