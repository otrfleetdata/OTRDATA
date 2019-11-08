from flask_restplus import Api, Resource, fields


from server.instance import server
from models.contact import contact

app, api = server.app, server.api

# Let's just keep them in memory 
contacts_db = [
    {"id": 0, "title": "War and Peace"},
    {"id": 1, "title": "Python for Dummies"},
]

# This class will handle GET and POST to /books
@api.route('/contact')
class ContactList(Resource):
    @api.marshal_list_with(contact)
    def get(self):
        return contacts_db

    # Ask flask_restplus to validate the incoming payload
    @api.expect(contact, validate=True)
    @api.marshal_with(contact)
    def post(self):
        # Generate new Id
        api.payload["id"] = contacts_db[-1]["id"] + 1 if len(contacts_db) > 0 else 0
        contacts_db.append(api.payload)
        return api.payload
# Handles GET and PUT to /books/:id
# The path parameter will be supplied as a parameter to every method
@api.route('/contacts/<int:id>')
class Contact(Resource):
    # Utility method
    def find_one(self, id):
        return next((b for b in contacts_db if b["id"] == id), None)

    @api.marshal_with(contact)
    def get(self, id):
        match = self.find_one(id)
        return match if match else ("Not found", 404)

    @api.marshal_with(contact)
    def delete(self, id):
        global contacts_db 
        match = self.find_one(id)
        contacts_db = list(filter(lambda b: b["id"] != id, contacts_db))
        return match

    # Ask flask_restplus to validate the incoming payload
    @api.expect(contact, validate=True)
    @api.marshal_with(contact)
    def put(self, id):
        match = self.find_one(id)
        if match != None:
            match.update(api.payload)
            match["id"] = id
        return match
