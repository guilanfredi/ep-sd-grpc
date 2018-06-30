from __future__ import print_function

import grpc

import simple_pb2
import simple_pb2_grpc

def run():
	num1 = 2
	num2 = 3

	channel = grpc.insecure_channel('localhost:50051')
	stub = simple_pb2_grpc.DelivererStub(channel)
	response = stub.MultiplyNumbers(simple_pb2.MultiplyRequest(a=num1, b=num2))
	print("%d x %d = %d" % (num1, num2, response.result))

if __name__ == '__main__':
	run()
