import sys
from concurrent import futures

import grpc

import service.library_pb2 as inventory_model_pb2
import service.inventory_service_pb2 as inventory_service_pb2
import service.inventory_service_pb2_grpc as inventory_service_pb2_grpc

books = {
    '1900023189': {
        'isbn': '1900023189',
        'title': 'Harry Potter',
        'author': 'JK Rowling',
        'genre': 'FANTASY',
        'year': 1997
    },
    '780091103': {
        'isbn': '780091103',
        'title': 'Da Vinci Code',
        'author': 'Dan Brown',
        'genre': 'MYSTERY',
        'year': 2003
    },
    '8193805013': {
        'isbn': '8193805013',
        'title': 'Born To Run',
        'author': 'Christopher McDougal',
        'genre': 'THRILLER',
        'year': 2011
    }
}


class InventoryServiceServicer(inventory_service_pb2_grpc.InventoryServiceServicer):
    status_invalid = inventory_model_pb2.Status(
        code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
        message=grpc.StatusCode.INVALID_ARGUMENT.name
    )
    status_exists = inventory_model_pb2.Status(
        code=grpc.StatusCode.ALREADY_EXISTS.value[0],
        message=grpc.StatusCode.ALREADY_EXISTS.name
    )
    status_notfound = inventory_model_pb2.Status(
        code=grpc.StatusCode.NOT_FOUND.value[0],
        message=grpc.StatusCode.NOT_FOUND.name
    )
    status_success = inventory_model_pb2.Status(
        code=grpc.StatusCode.OK.value[0],
    )

    def CreateBook(self, request, context):
        if not request.HasField('book'):
            return inventory_service_pb2.CreateBookReply(message="Missing new book details",
                                                            status=self.status_invalid)
        new_book = request.book

        if new_book.isbn == "" or new_book.title == "":
            return inventory_service_pb2.CreateBookReply(message="Missing ISBN or Title",
                                                            status=self.status_invalid)

        if new_book.isbn in books.keys():
            return inventory_service_pb2.CreateBookReply(message="Duplicate book",
                                                            status=self.status_exists)

        books[request.book.isbn] = {
            'isbn': new_book.isbn,
            'author': new_book.author,
            'title': new_book.title,
            'genre': inventory_model_pb2.Genre.Name(new_book.genre),
            'year': new_book.year
        }

        return inventory_service_pb2.CreateBookReply(message="Added book",
                                                     status=self.status_success)

    def GetBook(self, request, context):
        if request.isbn == "":
            return inventory_service_pb2.GetBookReply(status=self.status_invalid)

        if request.isbn not in books.keys():
            return inventory_service_pb2.GetBookReply(status=self.status_notfound)

        return inventory_service_pb2.GetBookReply(status=self.status_success, book=books[request.isbn])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_service_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServiceServicer(), server)

    port = '50051'
    server.add_insecure_port('[::]:' + port)

    server.start()
    print("Server started, listening on " + port)

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
