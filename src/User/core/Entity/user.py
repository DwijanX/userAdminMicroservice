class User:
    def __init__(self, userID, username, email, password):
        self.userID = userID
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(user_id={self.user_id}, username='{self.username}', email='{self.email}')"