from adapters.out.AuthenticationAdapter import AuthenticationAdapter
from adapters.out.MailServiceAdapter import MailServiceAdapter

class updateUsernamePort:
    def __init__(self):
        self.authAdapter=AuthenticationAdapter()
        self.mailAdapter=MailServiceAdapter()
    def updateUsername(self,userID,username,newUsername):
        self.authAdapter.changeUsername(userID,newUsername)
        self.mailAdapter.changeUsername(userID,newUsername)

