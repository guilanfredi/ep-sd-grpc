import xmlrpc.client
import time
import math
import sys

if __name__ == '__main__':

    logs = open("logs.txt", "w")

    s = xmlrpc.client.ServerProxy('http://localhost:8000')\

    long1 = math.floor(sys.maxsize / 10) + 1
    long2 = math.floor(sys.maxsize / 10) + 2
    long3 = math.floor(sys.maxsize / 10) + 3
    long4 = math.floor(sys.maxsize / 10) + 4
    long5 = math.floor(sys.maxsize / 10) + 5
    long6 = math.floor(sys.maxsize / 10) + 6
    long7 = math.floor(sys.maxsize / 10) + 7
    long8 = math.floor(sys.maxsize / 10) + 8

    # Vazio
    start_time = time.time() * 1000
    s.void()
    end_time = time.time() * 1000
    logs.write("Metodo: Sem parametros e sem retorno\n")
    logs.write("Parametros: Nenhum\n")
    logs.write("Resultado: Sem resultado\n")
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

    # Duplica Long
    start_time = time.time() * 1000
    resultado = int(s.dup(str(long1)))
    end_time = time.time() * 1000
    logs.write("Metodo: Duplicar um Long\n")
    logs.write("Parametros: {}\n".format(long1))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

    # Soma oito Longs
    start_time = time.time() * 1000
    resultado = int(s.add(str(long1), str(long2), str(long3), str(long4), str(long5), str(long6), str(long7), str(long8)))
    end_time = time.time() * 1000
    logs.write("Metodo: Soma de oito Longs\n")
    logs.write("Parametros: {},{},{},{},{},{},{},{}\n".format(long1, long2, long3, long4, long5, long6, long7, long8))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))


    string = "a"
    i = 0
    while(i < 10):
        string = string + string
        start_time = time.time() * 1000
        resultado = s.maximize(string)
        end_time = time.time() * 1000
        logs.write("Metodo: String to uppercase\n")
        logs.write("Parametros: 'aa...' Tamanho: {}\n".format(len(string)))
        logs.write("Resultado: 'AA...' Tamanho: {}\n".format(len(string)))
        logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))
        i = i + 1
