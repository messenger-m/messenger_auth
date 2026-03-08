# from app.utils import jwt as jwt_utils

class AuthService:
    def __init__(self):
        # Заглушка: только для примера
        self._users = {"user@example.com": "password123"}

    async def authenticate(self, login: str, password: str):
        if login not in self._users or self._users[login] != password:
            raise ValueError("Invalid credentials")
        # token, expires_at = jwt_utils.create_access_token(login)
        return "token", "expires_at"