import grpc

from service.inventory_service_pb2 import GetBookRequest
from service.inventory_service_pb2_grpc import InventoryServiceStub


# gRPC client for the Inventory Service which encapsulates the API
# It provides callable method get_book for retrieving a book from the inventory
class InventoryClient:
    def __init__(self, server_address, port):
        self.channel = grpc.insecure_channel(server_address + ':' + port)
        self.stub = InventoryServiceStub(self.channel) # The stub is generated

    # This function calls the GetBook function through the stub to retrieve a book by ISBN
    def get_book(self, isbn):
        try:
            response = self.stub.GetBook(GetBookRequest(isbn=isbn))

            return response.book
        except grpc.RpcError as err:
            if grpc.StatusCode.INVALID_ARGUMENT == err.code():
                print("Invalid arguments")
            elif grpc.StatusCode.NOT_FOUND == err.code():
                print("Book not found")
            else:
                print("Error with RPC request")
