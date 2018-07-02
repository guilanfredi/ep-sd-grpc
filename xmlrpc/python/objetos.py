class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # def getNome(self):
    #     return self.nome

    # def getIdade(self):
    #     return self.idade


class Endereco(object):
    def __init__(self, cidade, rua, numero):
        self.cidade = cidade
        self.rua = rua
        self.numero = numero

    # def getCidade(self):
    #     return self.cidade

    # def getRua(self):
    #     return self.rua

    # def getNumero(self):
    #     return self.numero


class Resposta(object):
    def __init__(self, id_retorno, hora):
        self.id = id_retorno
        self.hora = hora
