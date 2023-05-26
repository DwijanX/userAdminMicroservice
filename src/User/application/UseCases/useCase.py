# app/core/use_cases/user_use_case.py
from core.Entity.user import User
from adapters.repositories.userRespository import UserRepository

class CrudUserCase:
    def __init__(self):
        self.userRepository = UserRepository.getInstance()

    def createUser(self, username: str, email: str, password: str) -> User:
        user = User(None, username, email, password)
        return self.userRepository.create(user)

    def getUser(self, user_id: int) -> User:
        return self.userRepository.get_by_id(user_id)

    def updateUser(self, user_id: int, username: str, email: str, password: str) -> User:
        user = self.userRepository.get_by_id(user_id)
        if user:
            user.username = username
            user.email = email
            user.password = password
            return self.userRepository.update(user)
        return None

    def deleteUser(self, user_id: int) -> None:
        self.userRepository.delete(user_id)