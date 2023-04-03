from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os
import places_api as places
app = Flask(__name__)
#api = Api(app)

@app.route("/")
def index():
    return places.get_locations()

@app.route("/schedule")
def sheduled_location_update():
    pass

@app.route("/manual")
def manual_location_update():
    pass

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
