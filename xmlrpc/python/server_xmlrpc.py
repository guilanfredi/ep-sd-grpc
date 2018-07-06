from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from objetos import Pessoa, Endereco, Resposta, Retangulo
import sqlite3
import time
from datetime import datetime

# RPC Paths/Handler
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Criando o servidor
with SimpleXMLRPCServer(('192.168.1.116', 8000), requestHandler=RequestHandler, allow_none=True) as server:

    def void_function():
        a = 2 + 3
        print(a)

    def adder_function(a, b, c=0, d=0, e=0, f=0, g=0, h=0):
        return str(int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h))

    def duplicate_function(a):
        return str(int(a) * 2)

    def maximizeString_function(a):
        return a.upper()

    def criaPessoa(pessoa, endereco):
        try:
            path = './database.db'
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS pessoas (id_pessoa integer  PRIMARY KEY,nome text NOT NULL, idade integer NOT NULL)')
            c.execute('CREATE TABLE IF NOT EXISTS enderecos (id_endereco integer PRIMARY KEY,cidade text NOT NULL, rua text NOT NULL, numero integer NOT NULL)')
            c.execute('CREATE TABLE IF NOT EXISTS mora (id_pessoa integer NOT NULL,id_endereco integer NOT NULL,FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa),FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco))')
        except Exception:
            raise

        try:
            c.execute('INSERT INTO pessoas(nome,idade) VALUES (?, ?)',[pessoa['nome'], pessoa['idade']])
            id_pessoa = c.lastrowid
            c.execute('INSERT INTO enderecos(cidade, rua, numero) VALUES (?, ?, ?)',[endereco['cidade'], endereco['rua'], endereco['numero']])
            id_endereco = c.lastrowid
            c.execute('INSERT INTO mora (id_pessoa,id_endereco) VALUES ({}, {})'.format(id_pessoa, id_endereco))
            hora = datetime.now()
            conn.commit()
            c.close()
        except Exception:
            raise

        resposta = Resposta(id_pessoa, hora)
        return resposta

    def adicionaEndereco(endereco):
        try:
            path = './database.db'
            conn = sqlite3.connect(path)
            c = conn.cursor()
            id_pessoa = 1
            c.execute('INSERT INTO enderecos(cidade, rua, numero) VALUES (?, ?, ?)',[endereco['cidade'], endereco['rua'], endereco['numero']])
            id_endereco = c.lastrowid
            c.execute('INSERT INTO mora (id_pessoa,id_endereco) VALUES ({}, {})'.format(id_pessoa, id_endereco))
            hora = datetime.now()
            conn.commit()
            c.close()
        except Exception:
            raise

        resposta = Resposta(id_endereco, hora)
        return resposta

    def esticaRetangulo(retangulo):
        return Retangulo(retangulo['base'] * 2, retangulo['altura'])

    # Registrando as funcoes
    server.register_function(adder_function, 'add')
    server.register_function(duplicate_function, 'dup')
    server.register_function(void_function, 'void')
    server.register_function(maximizeString_function, 'maximize')
    server.register_function(criaPessoa, 'criaPessoa')
    server.register_function(adicionaEndereco, 'adicionaEndereco')
    server.register_function(esticaRetangulo, 'esticaRetangulo')

    # Rodando o servidor
    server.serve_forever()
