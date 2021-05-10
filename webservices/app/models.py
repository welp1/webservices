import os
from hashlib import scrypt

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(30))
    car_id = db.Column(db.Integer, nullable=False)
    owner = db.relationship('Owner', backref='cars', lazy=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))

    def to_dict_without_owners(self):
        return {'id': self.id, 'model': self.model, 'manufacturer': self.manufacturer, 'color': self.color, 'car_id': self.car_id}

    def to_dict(self):
        return {'id': self.id, 'model': self.model, 'manufacturer': self.manufacturer, 'color': self.color, 'car_id': self.car_id, 'owner': self.owner.to_dict_without_cars()}

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.Integer, nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    def to_dict_without_cars(self):
        return {'id': self.id, 'first_name': self.first_name, 'second_name': self.second_name, 'last_name': self.last_name}

    def to_dict(self):
        cars = []
        for s in self.cars:
            cars.append(s.to_dict_without_owners())
        return {'id': self.id, 'first_name': self.first_name, 'second_name': self.second_name, 'last_name':self.last_name, 'cars':cars}






