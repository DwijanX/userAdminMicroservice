class UserDTO:
    def __init__(self,userId=None, username=None, email=None):
        self.userId = userId
        self.username = username
        self.email = email

    @staticmethod
    def fromEntity(user):
        return UserDTO(
            username=user.username,
            email=user.email
        )