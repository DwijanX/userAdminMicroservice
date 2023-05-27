from adapters.out.AuthenticationAdapter import AuthenticationAdapter
from adapters.out.BillingServiceAdapter import BillingServiceAdapter
from adapters.out.MailServiceAdapter import MailServiceAdapter

class updateUsernamePort:
    def __init__(self):
        self.authAdapter=AuthenticationAdapter()
        self.billingAdapter=BillingServiceAdapter()
        self.mailAdapter=MailServiceAdapter()
    def updateUsername(self,userID,username):
        self.authAdapter.changeUsername(userID,username)
        self.billingAdapter.changeUsername(userID,username)
        self.mailAdapter.changeUsername(userID,username)

