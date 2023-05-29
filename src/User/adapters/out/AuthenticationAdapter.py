import requests

class AuthenticationAdapter:
    def __init__(self):
        self.baseUrl = "https://4197-181-177-147-247.ngrok-free.app/"

    def changeUsername(self, userID, newUsername):
        endpoint = '/update_username/'+str(userID)
        url = self.baseUrl + endpoint
        
        payload = {
            'new_username': newUsername
        }

        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                print("Username changed successfully.")
            else:
                print("Failed to change username. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
    def registerUser(self,userID,username,password):
        endpoint = '/register'
        url = self.baseUrl + endpoint

        payload = {
            "userID":userID,
            'username': username,
            'password': password
        }
        print(payload)
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("User registered in auth service successfully.")
            else:
                print("Failed to register user in auth service. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
    def deleteUser(self,userID):
        endpoint = '/delete/'+str(userID)
        url = self.baseUrl + endpoint        
        try:
            response = requests.delete(url)
            if response.status_code == 200:
                print("User deleted successfully.")
            else:
                print("Failed to delete user. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))