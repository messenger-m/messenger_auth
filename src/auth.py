import auth_pb2
import auth_pb2_grpc


class AuthServiceServicer(auth_pb2_grpc.AuthServiceServicer):

    async def Login(self, request, context):
        print(f"Login request: {request.username}, {request.password}")
        return auth_pb2.LoginResponse(
            token="jwt_example_123",
            refresh_token="refresh_example_123"
        )

    async def Register(self, request, context):
        print(f"Register request: {request.username}, {request.password}")
        # Здесь можно проверить пользователя, записать в БД, сгенерировать JWT и т.д.
        return auth_pb2.RegisterReply(
            success=True,
            message="User registered successfully"
        )