from application.Port.In.crudUseCase import CrudUserCase
from core.Entity.user import User
from adapters.DTO.userDTO import UserDTO
from application.Port.out.createUserPort import createUserPort
from application.Port.out.usernameUpdatePort import updateUsernamePort
from application.Port.out.deleteUserPort import DeleteUserPort

class UserService:
    def __init__(self):
        self.userUseCase = CrudUserCase()

    def createUser(self, userDTO: UserDTO) -> User:
        createdUser= self.userUseCase.createUser(userDTO.username, userDTO.email)
        if createdUser:
            createUserPort().createUser(createdUser.userID,createdUser.username,userDTO.password)
        return createdUser

    def getUser(self, userDTO: UserDTO) -> User:
        return self.userUseCase.getUser(userDTO.userId)

    def updateUser(self, userDTO: UserDTO) -> User:
        modifiedUser= self.userUseCase.updateUser(userDTO.userId,userDTO.username, userDTO.email)
        if modifiedUser:
            updateUsernamePort().updateUsername(userDTO.userId,userDTO.username)
        return modifiedUser

    def deleteUser(self, userDTO: UserDTO) -> None:
        self.userUseCase.deleteUser(userDTO.userId)
        DeleteUserPort().deleteUser(userDTO.userId)