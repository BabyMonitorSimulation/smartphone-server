import eventlet
eventlet.monkey_patch()
import os
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


try:
    os.remove("appSmartphone.db")
except Exception:
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///appSmartphone.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
socketio = SocketIO(app, async_mode='eventlet')
CORS(app)

from .controllers import main_controller
from .model import smartphone_model

db.create_all()
