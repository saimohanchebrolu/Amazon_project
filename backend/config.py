class Config:

    SECRET_KEY = "amazon-secret-key"

    JWT_SECRET_KEY = "amazon-jwt-secret"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:password@localhost:3306/amazon_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
