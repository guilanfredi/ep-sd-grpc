from concurrent import futures
import time

import grpc

import simple_pb2
import simple_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Deliverer(simple_pb2_grpc.DelivererServicer):
	
	def SumNumbers(self, request, context):
		aux = request.a + request.b
		return simple_pb2.SumResponse(result=aux)
	
	def SumOnServer(self, request, context):
		aux = 2 + 3
		print(aux)
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
