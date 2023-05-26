from application.UseCases.useCase import CrudUserCase
from core.Entity.user import User

class UserService:
    def __init__(self):
        self.userUseCase = CrudUserCase()

    def createUser(self, username: str, email: str, password: str) -> User:
        return self.userUseCase.createUser(username, email, password)

    def getUser(self, user_id: int) -> User:
        return self.userUseCase.getUser(user_id)

    def updateUser(self, user_id: int, username: str, email: str, password: str) -> User:
        return self.userUseCase.updateUser(user_id, username, email, password)

    def deleteUser(self, user_id: int) -> None:
        self.userUseCase.deleteUser(user_id)