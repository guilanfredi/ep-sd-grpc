import xmlrpc.client
import time
import math

logs = open("logs.txt", "w")

def run():
    s = xmlrpc.client.ServerProxy('http://localhost:8000')\

    long1 = math.floor(sys.maxsize / 10)+1
    long2 = math.floor(sys.maxsize / 10)+2
    long3 = math.floor(sys.maxsize / 10)+3
    long4 = math.floor(sys.maxsize / 10)+4
    long5 = math.floor(sys.maxsize / 10)+5
    long6 = math.floor(sys.maxsize / 10)+6
    long7 = math.floor(sys.maxsize / 10)+7
    long8 = math.floor(sys.maxsize / 10)+8

    vazio(s)
    duplicaLong(s, long1)
    somaOitoLongs(s, long1, long2, long3, long4, long5, long6, long7, long8)

# Método Vazio
def vazio(s):
    start_time = time.time() * 1000
    resultado = s.void()
    end_time = time.time() * 1000
    logs.write("Metodo: Sem parametros e sem retorno\n")
    logs.write("Parametros: Nenhum.\n".format(a,b))
    logs.write("Resultado: Sem resultado.\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))


# Método Duplica Long
def duplicaLong(s, a):
    start_time = time.time() * 1000
    resultado = s.mul(a, 2)
    end_time = time.time() * 1000
    logs.write("Metodo: Duplicar um Long\n")
    logs.write("Parametros: {}\n".format(a))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))


# Método Soma oito Longs
def somaOitoLongs(s, a, b, c, d, e, f, g, h):
    start_time = time.time() * 1000
    resultado = s.add(a, b, c, d, e, f, g, h)
    end_time = time.time() * 1000
    logs.write("Metodo: Soma de oito Longs\n")
    logs.write("Parametros: {},{},{},{},{},{},{},{}\n".format(a, b, c, d, e, f, g, h))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

if __name__ == '__main__':
    run()
