from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os
import places_api as places
import gcp
app = Flask(__name__)


@app.route("/")
def index():
    return gcp.get_json()

@app.route("/schedule")
def sheduled_location_update():
    return gcp.create_json(places.get_locations())

@app.route("/manual")
def manual_location_update():
     return gcp.create_json(places.get_locations())

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
