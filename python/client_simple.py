from __future__ import print_function

import grpc

import simple_pb2
import simple_pb2_grpc

def run():
	
	channel = grpc.insecure_channel('localhost:50051')
	stub = simple_pb2_grpc.DelivererStub(channel)

	num1 = 2
	num2 = 3

	response = stub.SumNumbers(simple_pb2.SumRequest(a=num1, b=num2))
	print("\nSomar dois ints(%d, %d) retornou: %d" % (num1, num2, response.result))


if __name__ == '__main__':
	run()
