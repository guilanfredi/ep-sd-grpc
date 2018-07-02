import xmlrpc.client
import time
import math
import sys
from objetos import Pessoa, Endereco, Resposta

if __name__ == '__main__':

    logs = open("logs.txt", "w")
    s = xmlrpc.client.ServerProxy('http://localhost:8000')\

    # Vazio
    start_time = time.time() * 1000
    s.void()
    end_time = time.time() * 1000
    logs.write("Metodo: Sem parametros e sem retorno\n")
    logs.write("Parametros: Nenhum\n")
    logs.write("Resultado: Sem resultado\n")
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

    # Duplica Long
    long1 = math.floor(sys.maxsize / 10) + 1
    start_time = time.time() * 1000
    resultado = int(s.dup(str(long1)))
    end_time = time.time() * 1000
    logs.write("Metodo: Duplicar um Long\n")
    logs.write("Parametros: {}\n".format(long1))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

    # Soma oito Longs
    long2 = math.floor(sys.maxsize / 10) + 2
    long3 = math.floor(sys.maxsize / 10) + 3
    long4 = math.floor(sys.maxsize / 10) + 4
    long5 = math.floor(sys.maxsize / 10) + 5
    long6 = math.floor(sys.maxsize / 10) + 6
    long7 = math.floor(sys.maxsize / 10) + 7
    long8 = math.floor(sys.maxsize / 10) + 8
    start_time = time.time() * 1000
    resultado = int(s.add(str(long1), str(long2), str(long3), str(long4), str(long5), str(long6), str(long7), str(long8)))
    end_time = time.time() * 1000
    logs.write("Metodo: Soma de oito Longs\n")
    logs.write("Parametros: {},{},{},{},{},{},{},{}\n".format(long1, long2, long3, long4, long5, long6, long7, long8))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

    # Maximizar Strings
    string = "a"
    i = 0
    while(i <= 10):
        start_time = time.time() * 1000
        resultado = s.maximize(string)
        end_time = time.time() * 1000
        logs.write("Metodo: String to uppercase\n")

        if(len(string) > 2):
            logs.write("Parametros: '{}...' Tamanho: {}\n".format(string[:2], len(string)))
            logs.write("Resultado: '{}...' Tamanho: {}\n".format(resultado[:2], len(resultado)))
        else:
            logs.write("Parametros: '{}' Tamanho: {}\n".format(string, len(string)))
            logs.write("Resultado: '{}' Tamanho: {}\n".format(resultado, len(resultado)))

        logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

        string = string + string
        i = i + 1

    # Cria Pessoa
    pessoa = Pessoa("Rafael", 23)
    endereco = Endereco("Sao Paulo", "Higienopolis", 1048)
    start_time = time.time() * 1000
    resultado = s.criaPessoa(pessoa, endereco)
    end_time = time.time() * 1000
    logs.write("Metodo: Inserir pessoa (objeto) no banco de dados\n")
    logs.write("Parametros: {},{}\n".format(pessoa, endereco))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

    # Adiciona endereço na pessoa criada anteriormente
    enderecoNovo = Endereco("Sao Paulo", "Arlindo Bettio", 1000)
    start_time = time.time() * 1000
    resultado = s.adicionaEndereco(enderecoNovo)
    end_time = time.time() * 1000
    logs.write("Metodo: Inserir pessoa (objeto) no banco de dados\n")
    logs.write("Parametros: {}\n".format(endereco))
    logs.write("Resultado: {}\n".format(resultado))
    logs.write("Tempo de execucao: {} ms\n\n".format(math.floor(end_time - start_time)))

    logs.close()
