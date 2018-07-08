# EP - Sistemas Distribuídos
Avaliação e comparação entre duas implementações de mecanismos de RPC: [gRPC](https://grpc.io/) e [XML-RPC](http://xmlrpc.scripting.com/).

Este repositório contém implementações das mesmas chamadas de procedimento remoto usando o framework gRPC e XML-RPC com algumas adaptações se necessário.

## Antes de começar

### Pré requisitos
Para execução destes programas, você precisará da versão 3.4 ou maior do Python.

Verifique se você tem o `pip` na versão 9.0.1 ou maior:

`$ python -m pip install --upgrade pip`

### Instale o gRPC

`$ python -m pip install grpcio`

### Instale o gRPC tools (Opcional)

Se desejar fazer alterações no arquivo `simple.proto` com as definições de mensagem e procedimentos remotos e gerar o código em Python do cliente e servidor correspondentes, você vai precisar do gRPC Tools.

Para instalá-lo, execute:

`$ python -m pip install grpcio-tools googleapis-common-protos`

## Baixe o código

Botão "Clone or download" > "Download ZIP" e extraia os arquivos compactados no diretório desejado.

ou

`$ git clone https://github.com/guilanfredi/ep-sd-grpc.git`


## Execute o programa

Em ambas as implementações o programa cliente envia uma requisição para cada um dos métodos do servidor e registra informações sobre parâmetros, resultado e tempo de execução no arquivo `logs.txt`, em execuções consecutivas os logs novos serão concatenados no final do arquivo.

Se necessário, para melhor visualização, apague o arquivo `logs.txt` antes da execução do programa cliente.

#### Implementação gRPC:
```
// Ir para a pasta grpc\python
$ cd grpc\python

// Executar programa servidor
$ python server_simple.py

// Em outro terminal execute o programa cliente
$ python client_simple.py
```

#### Implementação XML-RPC:
```
// Ir para a pasta grpc\python
$ cd xmlrpc\python

// Executar programa servidor
$ python server_xmlrpc.py

// Em outro terminal execute o programa cliente
$ python client_xmlrpc.py
```

## Observações

#### gRPC:

Para alterar as definições de procedimentos remotos e mensagens, edite o arquivo `grpc/proto/simple.proto`. Mais informações sobre ele e outros do mesmo tipo em [Google Protocol Buffers Overview](https://developers.google.com/protocol-buffers/docs/overview).

Quando finalizar suas alterações execute o seguinte comando a partir da pasta `grpc/python`:

`$ python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/simple.proto`

Ele compila o Protocol Buffer e gera dois arquivos em python na mesma pasta com as definições de métodos e metaclasses que podem ser utilizadas em Python para realizar as chamadas.

## Autores
* Guilherme Carvalho
* Rafael Bortman
