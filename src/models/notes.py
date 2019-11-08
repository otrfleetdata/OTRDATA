# -*- coding: utf-8 -*-

from flask_restplus import fields,inputs
from server.instance import server

notes = server.api.model('Notes', {
    'id': fields.Integer(description='Id'),
    'Subject': fields.String(required=True, min_length=1, max_length=200, description='Note Subject'),
    'Description': fields.String(required=True, min_length=1, max_length=200, description='Note Description')}
    )
    