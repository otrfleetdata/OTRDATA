# -*- coding: utf-8 -*-

from flask_restplus import fields,inputs
from server.instance import server
from models.contact import contact

deal = server.api.model('Deal', {
    'id': fields.Integer(description='Id'),
    'name': fields.String(required=True, min_length=1, max_length=20, description='type'),
    'expected_value': fields.Integer(required=True, min_length=1, max_length=20, description='expected value of deal'),
    'probability': fields.Integer(required=True, min_length=1, max_length=20, description='expected value of deal'),
    'close_date': fields.Integer(required=True, min_length=0, max_length=10, description='Phone Number'),
    'milestone': fields.DateTime(required=True, description='Birth Date'), 
})

deal_contact = server.api.inherit('contact_list',contact,{
                'contacts': fields.List(fields.Nested(contact))}
                           )