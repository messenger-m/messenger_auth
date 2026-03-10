from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt
from utils.config import settings


class AuthService:
    def __init__(self):
        # Заглушка: только для примера
        self._users = {"user@example.com": "password123"}

    async def authenticate(self, login: str, password: str):
        if login not in self._users or self._users[login] != password:
            raise ValueError("Invalid credentials")
        # token, expires_at = jwt_utils.create_access_token(login)
        return "token", "expires_at"
    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode |= {"exp": expire}
        encoded_jwt = jwt.encode(
            to_encode,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
            )
        return encoded_jwt

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)