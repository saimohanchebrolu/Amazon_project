from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    create_access_token
)

from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    response, status = AuthService.register(request.json)

    return jsonify(response), status


@auth_bp.route("/login", methods=["POST"])
def login():

    user = AuthService.login(request.json)

    if isinstance(user, tuple):

        return jsonify(user[0]), user[1]

    access_token = create_access_token(identity=user.id)

    return jsonify({

        "message": "Login Successful",

        "token": access_token,

        "user": user.to_dict()

    })
