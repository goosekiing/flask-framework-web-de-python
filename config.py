import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = str(os.getenv("USER_SECRET_KEY"))

SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
        SGBD = str(os.getenv("SGBD")),
        usuario = str(os.getenv("DB_USER")),
        senha = str(os.getenv("DB_PASSWORD")),
        servidor = str(os.getenv("DB_SERVER")),
        database = str(os.getenv("DB_NAME"))
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads"
