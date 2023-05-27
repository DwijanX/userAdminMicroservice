import requests

class AuthenticationAdapter:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def changeUsername(self, oldUsername, newUsername):
        endpoint = '/changeUsername'
        url = self.baseUrl + endpoint

        payload = {
            'old_username': oldUsername,
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