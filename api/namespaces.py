from flask_restx import Namespace, fields, Model

# Define Namespace
user_ns: Namespace = Namespace('users', description='User operations')

# Define Model (Reusable across any file that imports user_ns)
user_model: Model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'fullname': fields.String(),
    'age': fields.Integer()
})
