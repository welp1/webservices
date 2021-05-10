from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.models import db, Car, Owner


# class UsersResource(Resource):
#     def post(self):
#         data = request.get_json()
#         user = User.query.filter_by(username=data['username']).first()
#         if user and user.hash_verify(data['password']):
#             token = ''  # TODO: create token
#             return {
#                 'success': True,
#                 'token': token
#             }
#         return {'success': False}

class OwnersResource(Resource):
    def get(self):
        result = Owner.query.all()
        return [g.to_dict() for g in result]

    def post(self):
        data = request.get_json()
        db.session.add(Owner(first_name=data['first_name'], second_name=data['second_name'], last_name=data['last_name']))
        db.session.commit()
        return {'success': True}

class OwnerResource(Resource):
    def get(self, owner_id):
        owner = Owner.query.get_or_404(owner_id)
        return owner.to_dict()

    def put(self, owner_id):
        data = request.get_json()
        owner = Owner.query.get(owner_id)
        owner.first_name = data.get('first_name')
        owner.second_name = data.get('second_name')
        owner.last_name = data.get('last_name')
        db.session.add(owner)
        db.session.commit()
        return {'success': True}

    def delete(self, owner_id):
        owner = Owner.query.get(owner_id)
        db.session.delete(owner)
        db.session.commit()
        return {'success': True}

class CarsResource(Resource):
    def get(self):
        result = Car.query.all()
        return [s.to_dict() for s in result]

    def post(self):
        data = request.get_json()
        owners = Owner.query.all()
        owner = Owner(first_name='', second_name=0, last_name='')
        for g in owners:
            if data['owner'] == g.first_name:
                owner = g
        if owner.first_name == '':
            return {'success': False}
        s = Car(manufacturer=data['manufacturer'], model=data['model'], color=data['color'], car_id=data['car_id'])
        s.owner = owner
        db.session.add(s)
        db.session.commit()
        return {'success': True}

class CarResource(Resource):
    def get(self, car_id):
        car = Car.query.get_or_404(car_id)
        return car.to_dict()

    def put(self, car_id):
        data = request.get_json()
        owners = Owner.query.all()
        owner = Owner(first_name='', second_name=0, last_name='')
        for g in owners:
            if data.get('owner') == g.first_name:
                owner = g
        if owner.first_name == '':
            return {'success': False}
        car = Car.query.get(car_id)
        car.manufacturer = data.get('manufacturer')
        car.model = data.get('model')
        car.color = data.get('color')
        car.car_id = data.get('car_id')
        car.owner = owner
        db.session.add(car)
        db.session.commit()
        return {'success': True}

    def delete(self, car_id):
        car = Car.query.get(car_id)
        db.session.delete(car)
        db.session.commit()
        return {'success': True}
