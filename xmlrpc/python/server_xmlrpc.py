from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# RPC Paths/Handler
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Criando o servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:

    def void_function():
        a = 2 + 3
        print(a)

    def adder_function(a, b, c=0, d=0, e=0, f=0, g=0, h=0):
        return str(int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h))

    def duplicate_function(a):
        return str(int(a) * 2)

    def maximizeString_function(a):
        return a.upper()

    server.register_function(adder_function, 'add')
    server.register_function(duplicate_function, 'dup')
    server.register_function(void_function, 'void')
    server.register_function(maximizeString_function, 'maximize')

    # Rodando o servidor
    server.serve_forever()