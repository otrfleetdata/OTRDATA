# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from flask_restplus import Api, Resource, fields
from server.instance import server
from models.notes import notes
app, api = server.app, server.api

# Let's just keep them in memory 
notes_db = [
    {"id": 0, "Subject": "War and Peace", "Description": ""},
    {"id": 1, "Subject": "War and Peace", "Description": ""},
]

# This class will handle GET and POST to /books
@api.route('/notes')
class NotesList(Resource):
    @api.marshal_list_with(notes)
    def get(self):
        return notes_db

    # Ask flask_restplus to validate the incoming payload
    @api.expect(notes, validate=True)
    @api.marshal_with(notes)
    def post(self):
        # Generate new Id
        api.payload["id"] = notes_db[-1]["id"] + 1 if len(notes_db) > 0 else 0
        notes_db.append(api.payload)
        return api.payload
# Handles GET and PUT to /books/:id
# The path parameter will be supplied as a parameter to every method
@api.route('/notes/<int:id>')
class Notes(Resource):
    # Utility method
    def find_one(self, id):
        return next((b for b in notes_db if b["id"] == id), None)

    @api.marshal_with(notes)
    def get(self, id):
        match = self.find_one(id)
        return match if match else ("Not found", 404)

    @api.marshal_with(notes)
    def delete(self, id):
        global notes_db 
        match = self.find_one(id)
        notes_db = list(filter(lambda b: b["id"] != id, notes_db))
        return match

    # Ask flask_restplus to validate the incoming payload
    @api.expect(notes, validate=True)
    @api.marshal_with(notes)
    def put(self, id):
        match = self.find_one(id)
        if match != None:
            match.update(api.payload)
            match["id"] = id
        return match
