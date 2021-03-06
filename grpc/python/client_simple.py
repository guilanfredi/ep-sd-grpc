from __future__ import print_function

import sys
import math
import time

import grpc

import simple_pb2
import simple_pb2_grpc

def run():
	
	# Criando canal de conexão e instanciando a classe stub
	# Para rodar em diferentes computadores colocar o IP da máquina na linha abaixo
	channel = grpc.insecure_channel('localhost:50051')
	stub = simple_pb2_grpc.DelivererStub(channel)

	# Instanciando parâmetros que serão usados nas chamadas
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


	# Abrindo arquivo de logs
	logs = open("logs.txt", "w")

	# Chamando método 1) Void
	start_time = time.time() * 1000
	stub.void_function(simple_pb2.Empty())
	end_time = time.time() * 1000
	logs.write("Metodo: Sem parametros e sem retorno\n")
	logs.write("Parametros: \n")
	logs.write("Resultado: \n")
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))
	
	# Chamando método 2) 1 Long
	start_time = time.time() * 1000
	response = stub.duplicate_function(simple_pb2.SumLongRequest(a=num1))
	end_time = time.time() * 1000
	logs.write("Metodo: Duplica um long\n")
	logs.write("Parametros: {}\n".format(num1))
	logs.write("Resultado: {}\n".format(response.result))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

	#Chamando método 3) 8 Longs
	start_time = time.time() * 1000
	response = stub.adder_function(simple_pb2.SumEightLongsRequest(a=num1, b=num2, c=num3, d=num4, e=num5, f=num6, g=num7, h=num8))
	end_time = time.time() * 1000
	logs.write("Metodo: Soma oito longs\n")
	logs.write("Parametros: {}, {}, {}, {}, {}, {}, {}, {}\n".format(num1,num2,num3,num4,num5,num6,num7,num8))
	logs.write("Resultado: {}\n".format(response.result))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))


	# Chamando métodos String 10 vezes sempre dobrando o tamanho da entrada
	firstString = "a"
	i = 0
	while(i <= 10):
		
		start_time = time.time() * 1000
		response = stub.maximizeString_function(simple_pb2.StringRequest(a=firstString))
		end_time = time.time() * 1000
		logs.write("Metodo: String to uppercase\n")

		# Formatando resultado para legibilidade
		if(len(firstString) > 2):
			logs.write("Parametros: '{}...' Tamanho: {}\n".format(firstString[:2], len(firstString)))
			logs.write("Resultado: '{}...' Tamanho: {}\n".format(response.result[:2], len(response.result)))
		else:
			logs.write("Parametros: '{}' Tamanho: {}\n".format(firstString, len(firstString)))
			logs.write("Resultado: '{}' Tamanho: {}\n".format(response.result, len(response.result)))

		logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))
		
		firstString = firstString + firstString
		i = i + 1

	# Chamando método 6) Pessoa
	pessoa = simple_pb2.Pessoa(nome="Guilherme", idade=23)
	endereco = simple_pb2.Endereco(cidade="Sao Paulo", rua="Maracas", numero=121)
	start_time = time.time() * 1000
	resultado = stub.criaPessoa(simple_pb2.PessoaEndereco(person=pessoa, address=endereco))
	end_time = time.time() * 1000
	logs.write("Metodo: Inserir pessoa (objeto) no banco de dados\n")
	logs.write("Parametros: \n{}\n".format(pessoa, endereco))
	logs.write("Resultado: \n{}\n".format(resultado))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

	# Chamando método 7) Endereco
	enderecoNovo = simple_pb2.Endereco(cidade="Sao Paulo", rua="Arlindo Bettio", numero=1000)
	start_time = time.time() * 1000
	resultado = stub.adicionaEndereco(enderecoNovo)
	end_time = time.time() * 1000
	logs.write("Metodo: Inserir endereco (objeto) no banco de dados\n")
	logs.write("Parametros: \n{}\n".format(endereco))
	logs.write("Resultado: \n{}\n".format(resultado))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

	# Chamando método 5) Retangulo
	retangulo = simple_pb2.Retangulo(base=15, altura=10)
	start_time = time.time() * 1000
	resultado = stub.esticaRetangulo(simple_pb2.RetanguloRequest(ret=retangulo))
	end_time = time.time() * 1000
	logs.write("Metodo: Esticar retangulo (objeto)\n")
	logs.write("Parametros: \n{}\n".format(simple_pb2.RetanguloRequest(ret=retangulo)))
	logs.write("Resultado: \n{}\n".format(resultado))
	logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

	logs.close()

if __name__ == '__main__':
	run()
