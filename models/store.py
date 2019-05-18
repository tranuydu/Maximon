from db import db
class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') #load lazy

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'id': self.id ,'name': self.name, 'items': [item.json() for item in self.items.all()]} #must load all the items from lazy loading before using it

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def getItems(cls):
        return {'items': [item.json() for item in cls.query.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
