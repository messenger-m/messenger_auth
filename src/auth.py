import auth_pb2
import auth_pb2_grpc
from services.auth_service import AuthService

class AuthServiceServicer(auth_pb2_grpc.AuthServiceServicer):

    async def Login(self, request, context):
        print(f"Login request: {request.username}, {request.password}")
        jwt_token = AuthService().create_access_token({"user_name": request.username})
        return auth_pb2.LoginResponse(
            token=jwt_token,
            # refresh_token="refresh_example_123"
        )

    async def Register(self, request, context):
        print(f"Register request: {request.username}, {request.password}")
        password_hash = AuthService().hash_password(request.password)
        return auth_pb2.RegisterReply(
            success=True,
            username=request.username,
            password=password_hash,
        )