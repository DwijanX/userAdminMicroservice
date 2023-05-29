import requests

class BillingServiceAdapter:
    def __init__(self):
        self.baseUrl = "https://5dbc-200-87-92-243.sa.ngrok.io/"


    def deleteUser(self,userID):
        endpoint = '/bills/deletefromuser/'+str(userID)
        url = self.baseUrl + endpoint        
        try:
            response = requests.delete(url)
            if response.status_code == 200:
                print("User deleted successfully.")
            else:
                print("Failed to delete user. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))