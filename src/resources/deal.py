# -*- coding: utf-8 -*-
from flask_restplus import Api, Resource, fields
from server.instance import server
from models.deal import deal

app, api = server.app, server.api

# Let's just keep them in memory 
deals_db = [
    {"id": 0, "title": "War and Peace"},
    {"id": 1, "title": "Python for Dummies"},
]

# This class will handle GET and POST to /books
@api.route('/deal')
class DealList(Resource):
    @api.marshal_list_with(deal)
    def get(self):
        return deals_db

    # Ask flask_restplus to validate the incoming payload
    @api.expect(deal, validate=True)
    @api.marshal_with(deal)
    def post(self):
        # Generate new Id
        api.payload["id"] = deals_db[-1]["id"] + 1 if len(deals_db) > 0 else 0
        contacts_db.append(api.payload)
        return api.payload
# Handles GET and PUT to /books/:id
# The path parameter will be supplied as a parameter to every method
@api.route('/deals/<int:id>')
class Deal(Resource):
    # Utility method
    def find_one(self, id):
        return next((b for b in contacts_db if b["id"] == id), None)

    @api.marshal_with(deal)
    def get(self, id):
        match = self.find_one(id)
        return match if match else ("Not found", 404)

    @api.marshal_with(deal)
    def delete(self, id):
        global deals_db 
        match = self.find_one(id)
        contacts_db = list(filter(lambda b: b["id"] != id, contacts_db))
        return match

    # Ask flask_restplus to validate the incoming payload
    @api.expect(deal, validate=True)
    @api.marshal_with(deal)
    def put(self, id):
        match = self.find_one(id)
        if match != None:
            match.update(api.payload)
            match["id"] = id
        return match
