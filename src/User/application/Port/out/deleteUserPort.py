from adapters.out.AuthenticationAdapter import AuthenticationAdapter
from adapters.out.BillingServiceAdapter import BillingServiceAdapter
from adapters.out.MailServiceAdapter import MailServiceAdapter

class DeleteUserPort:
    def __init__(self):
        self.authAdapter=AuthenticationAdapter()
        self.billingAdapter=BillingServiceAdapter()
        self.mailAdapter=MailServiceAdapter()
    def deleteUser(self,userID):
        self.authAdapter.deleteUser(userID)
        self.billingAdapter.deleteUser(userID)
        self.mailAdapter.deleteUser(userID)

