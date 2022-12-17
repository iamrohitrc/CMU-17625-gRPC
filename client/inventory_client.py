import grpc

from service.inventory_service_pb2_grpc import InventoryServiceStub
from service.inventory_service_pb2 import GetBookRequest

"""Encapsulation of grpc client"""
class InventoryServiceClient:

    """setting all technical details at class instantiaion"""
    def __init__(self, address, port) -> None:
        self.address = address
        self.port = port
        self.channel = grpc.insecure_channel(self.address + ':' + self.port)
        self.stub = InventoryServiceStub(self.channel)
        print("Client initialization completed")

    """Method to get details of a book if it exists based on isbn provided by client in request"""
    def get_book_details(self, isbn):
        try:
            getBookRequest = GetBookRequest(isbn=isbn)
            bookDetails = self.stub.GetBook(getBookRequest)
            print("Book details for isbn retrieved successfully")
            print(bookDetails)
            return bookDetails.book
        except grpc.RpcError as e:
            print("Failed to get book details")
            print("Error code: " + e.code())
            print("Error details: " + e.details())

