from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from extensions import db
from models.user import User
from namespaces import user_ns, user_model, api
from flask_restx import Resource



@user_ns.route('/')
class UserList(Resource):
    @user_ns.marshal_list_with(user_model) # Documents the list response
    def get(self):
        return User.query.all()

    @user_ns.expect(user_model) # Documents the expected POST body
    @user_ns.response(201, 'User created')
    @user_ns.response(409, 'Conflict')
    def post(self):
        data = request.get_json()
        new_user = User(
            username=data['username'], 
            email=data['email'], 
            fullname=data.get('fullname'), 
            age=data.get('age')
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created!"}, 201
        except IntegrityError:
            db.session.rollback()
            user_ns.abort(409, "Username or email already exists")

@user_ns.route('/<int:id>')
@user_ns.response(404, 'User not found')
@user_ns.param('id', 'The user identifier')
class UserItem(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, id):
        return User.query.get_or_404(id)

    @user_ns.expect(user_model)
    def put(self, id):
        user = User.query.get_or_404(id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.fullname = data.get('fullname', user.fullname)
        user.age = data.get('age', user.age)
        try:
            db.session.commit()
            return {"message": "User updated!"}
        except IntegrityError:
            db.session.rollback()
            user_ns.abort(409, "Conflict: Duplicate data")

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted!"}
    
# Add this at the bottom
api.add_namespace(user_ns)