from adapters.out.AuthenticationAdapter import AuthenticationAdapter
from adapters.out.BillingServiceAdapter import BillingServiceAdapter
from adapters.out.MailServiceAdapter import MailServiceAdapter
from core.Entity.user import User
class DeleteUserPort:
    def __init__(self):
        self.authAdapter=AuthenticationAdapter()
        self.billingAdapter=BillingServiceAdapter()
        self.mailAdapter=MailServiceAdapter()
    def deleteUser(self,userID,email):
        self.authAdapter.deleteUser(userID)
        self.billingAdapter.deleteUser(userID)
        self.mailAdapter.deleteUser(email)

