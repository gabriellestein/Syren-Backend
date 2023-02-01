from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os
app = Flask(__name__)
api = Api(app)

    
api.add_resource(Places, '/places')
