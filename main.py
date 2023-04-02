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
# AIzaSyAkZUo_b8eMR301uy2fPBLN4_gDV-tzAQ4
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
