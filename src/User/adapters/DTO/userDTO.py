class UserDTO:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @staticmethod
    def fromEntity(user):
        return UserDTO(
            username=user.username,
            email=user.email
        )