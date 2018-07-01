from __future__ import print_function

import sys
import math
import time

import grpc

import simple_pb2
import simple_pb2_grpc

def run():
	
	channel = grpc.insecure_channel('localhost:50051')
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
	logs.write("Tempo de execucao: {} ms\n\n".format(end_time - start_time))
	


	start_time = time.time() * 1000
	response = stub.SumLong(simple_pb2.SumLongRequest(a=num1, b=num2))
	end_time = time.time() * 1000
	logs.write("Metodo: Soma dois longs\n")
	logs.write("Parametros: {} e {}\n".format(num1,num2))
	logs.write("Resultado: {}\n".format(response.result))
	logs.write("Tempo de execucao: {} ms\n\n".format(end_time - start_time))



	start_time = time.time() * 1000
	response = stub.SumEightLongs(simple_pb2.SumEightLongsRequest(a=num1, b=num2, c=num3, d=num4, e=num5, f=num6, g=num7, h=num8))
	end_time = time.time() * 1000
	logs.write("Metodo: Soma oito longs\n")
	logs.write("Parametros: {}, {}, {}, {}, {}, {}, {}, {}\n".format(num1,num2,num3,num4,num5,num6,num7,num8))
	logs.write("Resultado: {}\n".format(response.result))
	logs.write("Tempo de execucao: {} ms\n\n".format(end_time - start_time))



	firstString = "aa"
	i = 0
	while(i < 10):
		firstString = firstString + firstString
		start_time = time.time() * 1000
		response = stub.StringReplace(simple_pb2.StringRequest(a=firstString))
		end_time = time.time() * 1000
		logs.write("Metodo: String to uppercase\n")
		logs.write("Parametros: 'aa...' Tamanho: {}\n".format(len(firstString)))
		logs.write("Parametros: 'AA...' Tamanho: {}\n".format(len(firstString)))
		logs.write("Tempo de execucao: {} ms\n\n".format(end_time - start_time))
		i = i + 1


	logs.close()

if __name__ == '__main__':
	run()
