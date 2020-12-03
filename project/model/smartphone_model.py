from project import db


class Smartphone(db.Model):
    __tablename__ = "smartphone"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    crying = db.Column(db.Boolean, nullable=False)
    sleeping = db.Column(db.Boolean, nullable=False)
    breathing = db.Column(db.Boolean, nullable=False)
    time_no_breathing = db.Column(db.Integer, nullable=False)
