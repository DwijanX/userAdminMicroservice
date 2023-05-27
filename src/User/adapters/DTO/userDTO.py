class UserDTO:
    def __init__(self,userId=None, username=None, email=None,password=None):
        self.userId = userId
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def fromEntity(user):
        return UserDTO(
            username=user.username,
            email=user.email
        )