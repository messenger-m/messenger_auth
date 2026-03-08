import asyncio
import grpc
import auth_pb2_grpc
from auth import AuthServiceServicer


async def serve():
    server = grpc.aio.server()
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceServicer(), server)
    server.add_insecure_port("[::]:50052")
    await server.start()
    print("Auth gRPC server running on 50052...")
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())