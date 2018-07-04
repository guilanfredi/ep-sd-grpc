from __future__ import print_function

import sys
import math
import time

import grpc

import simple_pb2
import simple_pb2_grpc

from objetos import Pessoa, Endereco

def run():
	
	channel = grpc.insecure_channel('192.168.1.116:50051')
	stub = simple_pb2_grpc.DelivererStub(channel)

	num1 = math.floor(sys.maxsize / 10)+1
	num2 = math.floor(sys.maxsize / 10)+2
	num3 = math.floor(sys.maxsize / 10)+3
	num4 = math.floor(sys.maxsize / 10)+4
	num5 = math.floor(sys.maxsize / 10)+5
	num6 = math.floor(sys.maxsize / 10)+6
	num7 = math.floor(sys.maxsize / 10)+7
	num8 = math.floor(sys.maxsize / 10)+8
	start_time = time.time()
	end_time = time.time()
	response = 0


	stub.VoidOnServer(simple_pb2.Empty())

	logs = open("logs.txt", "w")

	start_time = time.time() * 1000
	stub.VoidOnServer(simple_pb2.Empty())
	end_time = time.time() * 1000
	logs.write("Metodo: Sem parametros e sem retorno\n")
	logs.write("Parametros: \n")
	logs.write("Resultado: \n")
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))
	


	start_time = time.time() * 1000
	response = stub.SumLong(simple_pb2.SumLongRequest(a=num1, b=num2))
	end_time = time.time() * 1000
	logs.write("Metodo: Soma dois longs\n")
	logs.write("Parametros: {} e {}\n".format(num1,num2))
	logs.write("Resultado: {}\n".format(response.result))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))



	start_time = time.time() * 1000
	response = stub.SumEightLongs(simple_pb2.SumEightLongsRequest(a=num1, b=num2, c=num3, d=num4, e=num5, f=num6, g=num7, h=num8))
	end_time = time.time() * 1000
	logs.write("Metodo: Soma oito longs\n")
	logs.write("Parametros: {}, {}, {}, {}, {}, {}, {}, {}\n".format(num1,num2,num3,num4,num5,num6,num7,num8))
	logs.write("Resultado: {}\n".format(response.result))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))



	firstString = "a"
	i = 0
	while(i < 10):
		
		start_time = time.time() * 1000
		response = stub.StringReplace(simple_pb2.StringRequest(a=firstString))
		end_time = time.time() * 1000
		logs.write("Metodo: String to uppercase\n")

		if(len(firstString) > 2):
			logs.write("Parametros: '{}...' Tamanho: {}\n".format(firstString[:2], len(firstString)))
			logs.write("Resultado: '{}...' Tamanho: {}\n".format(response.result[:2], len(response.result)))
		else:
			logs.write("Parametros: '{}' Tamanho: {}\n".format(firstString, len(firstString)))
			logs.write("Resultado: '{}' Tamanho: {}\n".format(response.result, len(response.result)))

		logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))
		
		firstString = firstString + firstString
		i = i + 1


	pessoa = simple_pb2.Pessoa(nome="Guilherme", idade=23)
	endereco = simple_pb2.Endereco(cidade="Sao Paulo", rua="Maracas", numero=121)
	start_time = time.time() * 1000
	resultado = stub.ComplexObjectOperation(simple_pb2.PessoaEndereco(person=pessoa, address=endereco))
	end_time = time.time() * 1000
	logs.write("Metodo: Inserir pessoa (objeto) no banco de dados\n")
	logs.write("Parametros: \n{}\n".format(pessoa, endereco))
	logs.write("Resultado: \n{}\n".format(resultado))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))


	enderecoNovo = simple_pb2.Endereco(cidade="Sao Paulo", rua="Arlindo Bettio", numero=1000)
	start_time = time.time() * 1000
	resultado = stub.AddAddress(enderecoNovo)
	end_time = time.time() * 1000
	logs.write("Metodo: Inserir endereco (objeto) no banco de dados\n")
	logs.write("Parametros: \n{}\n".format(endereco))
	logs.write("Resultado: \n{}\n".format(resultado))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))


	logs.close()

if __name__ == '__main__':
	run()
