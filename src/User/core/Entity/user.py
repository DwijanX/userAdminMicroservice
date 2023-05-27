class User:
    def __init__(self, userID, username, email):
        self.userID = userID
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(user_id={self.user_id}, username='{self.username}', email='{self.email}')"