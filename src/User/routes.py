# app/routes.py
from flask import Flask

from adapters.controllers.userController import userBP

app = Flask(__name__)
app.register_blueprint(userBP)

app.run()