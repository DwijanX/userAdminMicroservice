from adapters.out.AuthenticationAdapter import AuthenticationAdapter
from adapters.out.BillingServiceAdapter import BillingServiceAdapter
from adapters.out.MailServiceAdapter import MailServiceAdapter

class createUserPort:
    def __init__(self):
        self.authAdapter=AuthenticationAdapter()
    def createUser(self,userID,username,password):
        self.authAdapter.registerUser(userID,username,password)
