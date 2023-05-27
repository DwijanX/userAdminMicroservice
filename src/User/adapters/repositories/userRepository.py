import mysql.connector
from core.Entity.user import User
import yaml 

class UserRepository:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    @staticmethod
    def getInstance():
        configFile = 'src/User/config/userRepository.yaml'
        with open(configFile) as f:
            config = yaml.safe_load(f)
        host = config['host']
        username = config['username']
        password = config['password']
        database = config['database']
        return UserRepository(host,username,password,database)
    def __connectToDB__(self):
        connection = mysql.connector.connect(
        host=self.host,
        user=self.username,
        password=self.password,
        database=self.database
        )
        return connection
    def create(self, user: User) -> User:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        values = (user.username, user.email)
        cursor.execute(insert_query, values)
        userID = cursor.lastrowid
        user.userID = userID
        connection.commit()
        cursor.close()
        connection.close()
        return user

    def get_by_id(self, userID: int) -> User:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        select_query = "SELECT username, email FROM users WHERE userID = %s"
        cursor.execute(select_query, (userID,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            username, email = result
            return User(userID, username, email)
        return None

    def update(self, user: User) -> User:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        update_query = "UPDATE users SET username = %s, email = %s WHERE userID = %s"
        values = (user.username, user.email, user.userID)
        cursor.execute(update_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return user

    def delete(self, userID: int) -> None:
        print("llega")
        print(type(userID))
        connection = self.__connectToDB__()
        cursor = connection.cursor()
        delete_query = "DELETE FROM users WHERE userID = %s"
        cursor.execute(delete_query, (userID,))
        connection.commit()
        cursor.close()
        connection.close()