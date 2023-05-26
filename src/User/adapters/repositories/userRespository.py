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
        configFile = r'config\ruserRepository.yaml'
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
        insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (user.username, user.email, user.password)
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
        select_query = "SELECT username, email, password FROM users WHERE user_id = %s"
        cursor.execute(select_query, (userID,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            username, email, password = result
            return User(userID, username, email, password)
        return None

    def update(self, user: User) -> User:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        update_query = "UPDATE users SET username = %s, email = %s, password = %s WHERE user_id = %s"
        values = (user.username, user.email, user.password, user.user_id)
        cursor.execute(update_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return user

    def delete(self, user_id: int) -> None:
        connection = self.__connectToDB__()
        cursor = connection.cursor()
        delete_query = "DELETE FROM users WHERE user_id = %s"
        cursor.execute(delete_query, (user_id,))
        connection.commit()
        cursor.close()
        connection.close()