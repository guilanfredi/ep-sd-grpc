from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# RPC Paths/Handler
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Criando o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:

    def void_function():
        a = 2 + 3
    def adder_function(a,b,c=0,d=0,e=0,f=0,g=0,h=0):
        return a + b + c + d + e + f + g + h
    def duplicate_function(a):
        return a*2




    server.register_function(adder_function, 'add')
    server.register_function(void_function, 'add')

    # Rodando o servidor
    server.serve_forever()