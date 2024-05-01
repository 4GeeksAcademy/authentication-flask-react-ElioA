"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route("/user", methods=["GET"])
def get_users():
    users= User.query.all()
    all_users= list(map(lambda x: x.serialize(), users))
    return jsonify(all_users), 200


@api.route("/singup", methods=["POST"])
def create_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
   
    if email is None:
        return jsonify({"msg":"email should be in New User Body"}), 400
    if password is None:
        return jsonify({"msg": "Password can not be empty"}), 400
    

    new_user = User(
        email = email,
        password = password,
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg" : "new user created"})


@api.route("/login", methods=["POST"])
def authenticate_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email, password=password).first()

    if user is None:
        return jsonify({"msg": "Email or Password is Wrong!"}), 401
    
    jwt_token = create_access_token(identity=user.id)
    return jsonify({ "token": jwt_token, "user_id": user.id })

@api.route('/private', methods=['POST', 'GET'])
@jwt_required()
def handle_hello():

    response_body = {
        "message": "you have succesfully loged in, congratulations"
    }

    return jsonify(response_body), 200

