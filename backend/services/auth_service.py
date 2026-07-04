import bcrypt

from database import db
from models.user import User


class AuthService:

    @staticmethod
    def register(data):

        user = User.query.filter_by(email=data["email"]).first()

        if user:

            return {"message": "Email already exists"}, 400

        hashed_password = bcrypt.hashpw(
            data["password"].encode(),
            bcrypt.gensalt()
        ).decode()

        new_user = User(
            first_name=data["first_name"],
            last_name=data.get("last_name"),
            email=data["email"],
            password=hashed_password,
            phone=data.get("phone")
        )

        db.session.add(new_user)

        db.session.commit()

        return {"message": "User Registered Successfully"}, 201

    @staticmethod
    def login(data):

        user = User.query.filter_by(email=data["email"]).first()

        if not user:

            return {"message": "Invalid Credentials"}, 401

        if not bcrypt.checkpw(
            data["password"].encode(),
            user.password.encode()
        ):

            return {"message": "Invalid Credentials"}, 401

        return user
