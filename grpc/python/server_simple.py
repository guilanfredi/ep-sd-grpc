from concurrent import futures
import time
from datetime import datetime

import grpc

import simple_pb2
import simple_pb2_grpc

import sqlite3

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Deliverer(simple_pb2_grpc.DelivererServicer):
	
	def VoidOnServer(self, request, context):
		aux = 2 + 3
		return simple_pb2.Empty()
	
	def SumLong(self, request, context):
		aux = request.a + request.b
		return simple_pb2.SumLongResponse(result=aux)
	
	def SumEightLongs(self, request, context):
		aux = request.a + request.b + request.c + request.d + request.e + request.f + request.g + request.h 
		return simple_pb2.SumLongResponse(result=aux)
	
	def StringReplace(self, request, context):
		aux = request.a.upper()
		return simple_pb2.StringResponse(result=aux)
	
	def ComplexObjectOperation(self, request, context):
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
			c.execute('INSERT INTO pessoas(nome,idade) VALUES (?, ?)',[request.person.nome, request.person.idade])
			id_pessoa = c.lastrowid
			c.execute('INSERT INTO enderecos(cidade, rua, numero) VALUES (?, ?, ?)',[request.address.cidade, request.address.rua, request.address.numero])
			id_endereco = c.lastrowid
			c.execute('INSERT INTO mora (id_pessoa,id_endereco) VALUES (?, ?)', [id_pessoa, id_endereco])
			hora = datetime.now()
			conn.commit()
		except Exception:
			raise

		resposta = simple_pb2.PessoaResposta(id_pessoa=id_pessoa, hora=hora.strftime("%Y-%m-%d %H:%M:%S"))
		return resposta



def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	simple_pb2_grpc.add_DelivererServicer_to_server(Deliverer(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)


if __name__ == '__main__':
	serve()
