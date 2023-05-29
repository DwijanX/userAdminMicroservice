import requests

class MailServiceAdapter:
    def __init__(self):
        self.baseUrl = "https://de6b-200-87-92-94.ngrok-free.app/"

    def registerUser(self, userID):
        endpoint = '/send_email/Register'
        url = self.baseUrl + endpoint

        payload = {
            'id': userID
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Username registration mail sent")
            else:
                print("Failed to send registration user. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
    def changeUsername(self, userID, newUsername):
        endpoint = '/send_email/change_username/'+str(userID)
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
    def deleteUser(self,email):
        endpoint = '/send_email/user_deleted'
        url = self.baseUrl + endpoint   
        payload = {
            'email': email
        }     
        try:
            response = requests.delete(url,json=payload)
            if response.status_code == 200:
                print("User deleted successfully.")
            else:
                print("Failed to delete user. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))