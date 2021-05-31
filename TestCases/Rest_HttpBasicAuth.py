from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
api = Api(app, prefix = '/testget')
auth = HTTPBasicAuth()

USER_DATA = {"durvesh":"123@Abcde"}

@auth.verify_password
def verify(username,password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        return {"Meaning_of_life":42}

api.add_resource(PrivateResource, "/private")

app.run(debug= True)