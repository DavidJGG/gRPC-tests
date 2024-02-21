from concurrent import futures
import logging

import grpc
from grpc_generated import example_pb2
from grpc_generated import example_pb2_grpc


class Operacion(example_pb2_grpc.multiplicarServicer):
    def multiplicar(self, request, context):
        result = request.num1 * request.num2
        return example_pb2.multiplicarReply(resultado=result)
    
    def dividir(self, request, context):
        result = request.num1 / request.num2
        return example_pb2.multiplicarReply(resultado=int(result))
    
    def mega(self, request, context):
        result = "A" * request.size
        return example_pb2.megaReply(secuencia=result)
    
def server():
    port = "5001"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_multiplicarServicer_to_server(Operacion(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    server()