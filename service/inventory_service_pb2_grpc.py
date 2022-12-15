# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inventory_model_pb2 as inventory__model__pb2
import inventory_service_pb2 as inventory__service__pb2


class InventoryServiceStub(object):
    """Service to declare rpc methods
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/inventorySystem.InventoryService/CreateBook',
                request_serializer=inventory__model__pb2.Book.SerializeToString,
                response_deserializer=inventory__service__pb2.CreateBookResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/inventorySystem.InventoryService/GetBook',
                request_serializer=inventory__service__pb2.GetBookRequest.SerializeToString,
                response_deserializer=inventory__service__pb2.GetBookResponse.FromString,
                )


class InventoryServiceServicer(object):
    """Service to declare rpc methods
    """

    def CreateBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=inventory__model__pb2.Book.FromString,
                    response_serializer=inventory__service__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=inventory__service__pb2.GetBookRequest.FromString,
                    response_serializer=inventory__service__pb2.GetBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inventorySystem.InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Service to declare rpc methods
    """

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventorySystem.InventoryService/CreateBook',
            inventory__model__pb2.Book.SerializeToString,
            inventory__service__pb2.CreateBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventorySystem.InventoryService/GetBook',
            inventory__service__pb2.GetBookRequest.SerializeToString,
            inventory__service__pb2.GetBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
