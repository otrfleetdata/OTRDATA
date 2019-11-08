# -*- coding: utf-8 -*-
from server.instance import server
import sys, os

# Need to import all resources
# so that they register with the server 
from resources.contact import *
from resources.deal import *
from resources.notes import *

if __name__ == '__main__':
    server.run()