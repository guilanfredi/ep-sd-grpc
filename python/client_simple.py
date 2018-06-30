from __future__ import print_function

import sys
import math

import grpc

import simple_pb2
import simple_pb2_grpc

def run():
	
	channel = grpc.insecure_channel('localhost:50051')
	stub = simple_pb2_grpc.DelivererStub(channel)

	numa = 2
	numb = 3

	response = stub.SumNumbers(simple_pb2.SumRequest(a=numa, b=numb))
	print("\nSomar dois ints(%d, %d) retornou: %d" % (numa, numb, response.result))

	stub.SumOnServer(simple_pb2.Empty())
	print("\nSomar dois ints no servidor foi concluído")

	num1 = math.floor(sys.maxsize / 10)
	num2 = math.floor(sys.maxsize / 10)
	num3 = math.floor(sys.maxsize / 10)
	num4 = math.floor(sys.maxsize / 10)
	num5 = math.floor(sys.maxsize / 10)
	num6 = math.floor(sys.maxsize / 10)
	num7 = math.floor(sys.maxsize / 10)
	num8 = math.floor(sys.maxsize / 10)

	response = stub.SumLong(simple_pb2.SumLongRequest(a=num1, b=num2))
	print("\nSomar dois longs(%d, %d) retornou: %d" % (num1, num2, response.result))

	response = stub.SumEightLongs(simple_pb2.SumEightLongsRequest(a=num1, b=num2, c=num3, d=num4, e=num5, f=num6, g=num7, h=num8))
	print("\nSomar oito longs(%d, %d, %d, %d, %d, %d, %d, %d) retornou: %d" % (num1, num2, num3, num4, num5, num6, num7, num8, response.result))

	firstString = "aa"

	response = stub.StringReplace(simple_pb2.StringRequest(a=firstString))
	print("\n formatar string(%s) retornou: %s" % (firstString, response.result))

if __name__ == '__main__':
	run()
