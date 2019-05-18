from flask_restful import Resource, reqparse
from models.store import StoreModel
from flask_jwt import jwt_required

class Store(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store is not found'}, 404

    @jwt_required()
    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': "Store '{}' is already exists".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'AN error is occured while creating the store'}, 500
        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_to_db()
        return {'message': 'Store deleted'}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
