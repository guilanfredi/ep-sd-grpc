from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from objetos import Calculadora, Pessoa, Endereco, Resposta
import sqlite3
import time


# RPC Paths/Handler
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Criando o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler, allow_none=True) as server:

    def void_function():
        a = 2 + 3
        print(a)

    def adder_function(a, b, c=0, d=0, e=0, f=0, g=0, h=0):
        return str(int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h))

    def duplicate_function(a):
        return str(int(a) * 2)

    def maximizeString_function(a):
        return a.upper()

    def quadradoDoPrimeiroMenosQuadradodoSegundo(a, b):
        calc = Calculadora()
        add = calc.operacoes['soma'](a, b)
        sub = calc.operacoes['subtracao'](a, b)
        return add * sub

    def criaPessoa(pessoa, endereco):
        try:
            path = './database.db'
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS pessoas (id_pessoa integer AUTO_INCREMENT  PRIMARY KEY,nome text NOT NULL, idade integer NOT NULL)')
            c.execute('CREATE TABLE IF NOT EXISTS enderecos (id_endereco integer AUTO_INCREMENT PRIMARY KEY,cidade text NOT NULL, rua text NOT NULL, numero integer NOT NULL)')
            c.execute('CREATE TABLE IF NOT EXISTS mora (id_pessoa integer NOT NULL,id_endereco integer NOT NULL,FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa),FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco))')
        except Exception:
            raise

        try:
            c.execute('INSERT INTO pessoa (nome,idade) VALUES ({}, {})'.format(pessoa.getNome(), pessoa.getIdade()))
            id_pessoa = c.lastrowid
            c.execute('INSERT INTO endereco (cidade, rua, numero) VALUES ({}, {}, {})'.format(endereco.getCidade(), endereco.getRua(), endereco.getNumero()))
            id_endereco = c.lastrowid
            c.execute('INSERT INTO mora (id_pessoa,id_endereco) VALUES ({}, {})'.format(id_pessoa, id_endereco))
            hora = time.clock_realtime

        except Exception:
            raise

        resposta = Resposta(id_pessoa, hora)
        return resposta



    # Registrando as funcoes
    server.register_function(adder_function, 'add')
    server.register_function(duplicate_function, 'dup')
    server.register_function(void_function, 'void')
    server.register_function(maximizeString_function, 'maximize')
    server.register_function(quadradoDoPrimeiroMenosQuadradodoSegundo, 'quadradoDoPrimeiroMenosQuadradodoSegundo')
    server.register_function(criaPessoa, 'criaPessoa')

    # Rodando o servidor
    server.serve_forever()
