# app/core/use_cases/user_use_case.py
from core.Entity.user import User
from adapters.repositories.userRespository import UserRepository

class CrudUserCase:
    def __init__(self):
        self.userRepository = UserRepository.getInstance()

    def createUser(self, username: str, email: str) -> User:
        user = User(None, username, email)
        return self.userRepository.create(user)

    def getUser(self, userID: int) -> User:
        user=self.userRepository.get_by_id(userID)
        return user

    def updateUser(self, userID: int, username: str, email: str) -> User:
        user = self.userRepository.get_by_id(userID)
        if user:
            user.username = username
            user.email = email
            return self.userRepository.update(user)
        return None

    def deleteUser(self, userID: int) -> None:
        self.userRepository.delete(userID)