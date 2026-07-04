import os

class Config:

    SECRET_KEY = "amazon-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:password@localhost:3306/amazon_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
