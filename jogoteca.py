from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app=app)
csrf = CSRFProtect(app=app)
bcrypt = Bcrypt(app=app)

from views_game import *
from views_user import *

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000
    app.run(host=host, port=port, debug=True)
