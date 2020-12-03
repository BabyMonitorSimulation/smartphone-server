from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

try:
    os.remove("appSmartphone.db")
except Exception:
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///appSmartphone.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from .controllers import (
    main_controller
)
from .model import (
    smartphone_model
)

db.create_all()
