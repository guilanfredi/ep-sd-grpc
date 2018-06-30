from concurrent import futures
import time

import grpc

import simple_pb2
import simple_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Deliverer(simple_pb2_grpc.DelivererServicer):
	
	def MultiplyNumbers(self, request, context):
		return simple_pb2.MultiplyResponse(result=request.a * request.b)

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
