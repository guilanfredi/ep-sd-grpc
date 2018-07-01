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

	numa = 2
	numb = 3
	num1 = math.floor(sys.maxsize / 10)
	num2 = math.floor(sys.maxsize / 10)
	num3 = math.floor(sys.maxsize / 10)
	num4 = math.floor(sys.maxsize / 10)
	num5 = math.floor(sys.maxsize / 10)
	num6 = math.floor(sys.maxsize / 10)
	num7 = math.floor(sys.maxsize / 10)
	num8 = math.floor(sys.maxsize / 10)
	start_time = time.time()
	end_time = time.time()
	response = 0


	stub.SumOnServer(simple_pb2.Empty())


	start_time = time.time() * 1000
	stub.SumOnServer(simple_pb2.Empty())
	end_time = time.time() * 1000
	print("\nSomar dois ints no servidor foi concluído")
	print ("Runtime: {}ms\n".format(end_time- start_time))



	start_time = time.time() * 1000
	response = stub.SumNumbers(simple_pb2.SumRequest(a=numa, b=numb))
	end_time = time.time() * 1000
	print("\nSomar dois ints\nParams: (%d, %d)\nRetornou: %d" % (numa, numb, response.result))
	print ("Runtime: {}ms\n".format(end_time- start_time))



	start_time = time.time() * 1000
	response = stub.SumLong(simple_pb2.SumLongRequest(a=num1, b=num2))
	end_time = time.time() * 1000
	print("\nSomar dois longs\nParams: (%d, %d)\nRetornou: %d" % (num1, num2, response.result))
	print ("Runtime: {}ms\n".format(end_time- start_time))



	start_time = time.time() * 1000
	response = stub.SumEightLongs(simple_pb2.SumEightLongsRequest(a=num1, b=num2, c=num3, d=num4, e=num5, f=num6, g=num7, h=num8))
	end_time = time.time() * 1000
	print("\nSomar oito longs\nParams: (%d, %d, %d, %d, %d, %d, %d, %d)\nRetornou: %d" % (num1, num2, num3, num4, num5, num6, num7, num8, response.result))
	print ("Runtime: {}ms\n".format(end_time- start_time))



	firstString = "aa"
	start_time = time.time() * 1000	
	response = stub.StringReplace(simple_pb2.StringRequest(a=firstString))
	end_time = time.time() * 1000
	print("\nFormatar string\nParams: (%s)\nRetornou: %s" % (firstString, response.result))
	print ("Runtime: {}ms\n".format(end_time- start_time))


if __name__ == '__main__':
	run()
