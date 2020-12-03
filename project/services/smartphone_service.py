from project import db
from project.model.smartphone_model import Smartphone
from project.util.clean import clean_data


def insert_data(data):
    smartphone = Smartphone(**data)
    db.session.add(smartphone)
    db.session.commit()
    return smartphone


def last_record():
    return clean_data(Smartphone.query.all()[-1].__dict__)


'''def update_data(data):
    last_record = db.query.order_by(db.database.id.desc()).first()
    if data["crying"]:
        crying = {"crying": data["crying"]}
        Smartphone.query.filter_by(id=last_record.id).update(crying)
    if not data["breathing"]:
        time_no_breathing = {"time_no_breathing": data["time_no_breathing"]}
        Smartphone.query.filter_by(id=last_record.id).update(time_no_breathing)
    db.session.commit()


def get_by_id(id):
    return Smartphone.query.filter_by(id=id).first()
'''