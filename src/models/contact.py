# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from flask_restplus import fields,inputs
from server.instance import server

contact = server.api.model('Contact', {
    'id': fields.Integer(description='Id'),
    'Name': fields.String(required=True, min_length=1, max_length=200, description='Contact Name'),
    'Age': fields.Integer(required=True, min_length=1, max_length=200, description='Contact age'),
    'Phone Number': fields.Integer(required=True, min_length=0, max_length=10, description='Phone Number'),
    'Birth Date': fields.DateTime(required=True, description='Birth Date')
})

