from application.UseCases.useCase import CrudUserCase
from core.Entity.user import User
from adapters.DTO.userDTO import UserDTO

class UserService:
    def __init__(self):
        self.userUseCase = CrudUserCase()

    def createUser(self, userDTO: UserDTO) -> User:
        return self.userUseCase.createUser(userDTO.username, userDTO.email, userDTO.password)

    def getUser(self, userDTO: UserDTO) -> User:
        return self.userUseCase.getUser(userDTO.userId)

    def updateUser(self, userDTO: UserDTO) -> User:
        return self.userUseCase.updateUser(userDTO.userId, userDTO.username, userDTO.email, userDTO.password)

    def deleteUser(self, userDTO: UserDTO) -> None:
        self.userUseCase.deleteUser(userDTO.userId)