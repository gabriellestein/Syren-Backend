from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os
app = Flask(__name__)
api = Api(app)

app.route("/")
def index():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
