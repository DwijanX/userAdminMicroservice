import requests

class BillingServiceAdapter:
    def __init__(self):
        self.baseUrl = "baseUrl"

    def changeUsername(self, userID, newUsername):
        endpoint = '/changeUsername/'+str(userID)
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
    def deleteUser(self,userID):
        endpoint = '/deleteUser/'+str(userID)
        url = self.baseUrl + endpoint        
        try:
            response = requests.delete(url)
            if response.status_code == 200:
                print("User deleted successfully.")
            else:
                print("Failed to delete user. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))