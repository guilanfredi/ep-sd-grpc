# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import simple_pb2 as simple__pb2


class DelivererStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.VoidOnServer = channel.unary_unary(
        '/Deliverer/VoidOnServer',
        request_serializer=simple__pb2.Empty.SerializeToString,
        response_deserializer=simple__pb2.Empty.FromString,
        )
    self.SumLong = channel.unary_unary(
        '/Deliverer/SumLong',
        request_serializer=simple__pb2.SumLongRequest.SerializeToString,
        response_deserializer=simple__pb2.SumLongResponse.FromString,
        )
    self.SumEightLongs = channel.unary_unary(
        '/Deliverer/SumEightLongs',
        request_serializer=simple__pb2.SumEightLongsRequest.SerializeToString,
        response_deserializer=simple__pb2.SumLongResponse.FromString,
        )
    self.StringReplace = channel.unary_unary(
        '/Deliverer/StringReplace',
        request_serializer=simple__pb2.StringRequest.SerializeToString,
        response_deserializer=simple__pb2.StringResponse.FromString,
        )
    self.ComplexObjectOperation = channel.unary_unary(
        '/Deliverer/ComplexObjectOperation',
        request_serializer=simple__pb2.PessoaEndereco.SerializeToString,
        response_deserializer=simple__pb2.PessoaResposta.FromString,
        )
    self.AddAddress = channel.unary_unary(
        '/Deliverer/AddAddress',
        request_serializer=simple__pb2.Endereco.SerializeToString,
        response_deserializer=simple__pb2.PessoaResposta.FromString,
        )


class DelivererServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def VoidOnServer(self, request, context):
    """1)
    operação sem parâmetros e sem valor de retorno
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SumLong(self, request, context):
    """2)
    operação com um long de parâmetro e retorna um long
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SumEightLongs(self, request, context):
    """3)
    operação com um 8 valores long de parâmetro e retorna um long
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StringReplace(self, request, context):
    """4)
    operação com parâmetro string e valor de retorno string
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ComplexObjectOperation(self, request, context):
    """5) Operação que passa um tipo complexo e retorna outro tipo complexo
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddAddress(self, request, context):
    """Insere um endereço no banco de dados e retorna seu id e uma data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DelivererServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'VoidOnServer': grpc.unary_unary_rpc_method_handler(
          servicer.VoidOnServer,
          request_deserializer=simple__pb2.Empty.FromString,
          response_serializer=simple__pb2.Empty.SerializeToString,
      ),
      'SumLong': grpc.unary_unary_rpc_method_handler(
          servicer.SumLong,
          request_deserializer=simple__pb2.SumLongRequest.FromString,
          response_serializer=simple__pb2.SumLongResponse.SerializeToString,
      ),
      'SumEightLongs': grpc.unary_unary_rpc_method_handler(
          servicer.SumEightLongs,
          request_deserializer=simple__pb2.SumEightLongsRequest.FromString,
          response_serializer=simple__pb2.SumLongResponse.SerializeToString,
      ),
      'StringReplace': grpc.unary_unary_rpc_method_handler(
          servicer.StringReplace,
          request_deserializer=simple__pb2.StringRequest.FromString,
          response_serializer=simple__pb2.StringResponse.SerializeToString,
      ),
      'ComplexObjectOperation': grpc.unary_unary_rpc_method_handler(
          servicer.ComplexObjectOperation,
          request_deserializer=simple__pb2.PessoaEndereco.FromString,
          response_serializer=simple__pb2.PessoaResposta.SerializeToString,
      ),
      'AddAddress': grpc.unary_unary_rpc_method_handler(
          servicer.AddAddress,
          request_deserializer=simple__pb2.Endereco.FromString,
          response_serializer=simple__pb2.PessoaResposta.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Deliverer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
