from flask import Blueprint
from flask_restx import Api, Namespace, fields

# 1. Blueprint for the API
api_bp = Blueprint('api', __name__)

# 2. Api object (leave constructor empty to avoid early binding)
api = Api(title='My API', version='1.0', description='User API', doc='/')
api.contact = {
    "name": "Joseph",   
    "url": "https://your-website.com",
    "email": "your-email@example.com"
}
api.license = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT"
}
api.terms_url = "https://your-website.com/terms"


# 3. Your Namespace
user_ns = Namespace('users', description='User operations')

user_model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'fullname': fields.String(),
    'age': fields.Integer()
})
