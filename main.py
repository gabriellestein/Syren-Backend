from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os
app = Flask(__name__)
#api = Api(app)

@app.route("/")
def index():
    text = "Hello my name is Syren, I'm here to help! I can help you find emergancy resources in your area. This includes: Police Stations, Hospitals, Foods banks, shelters, recycling centers, mental health resources, and so much more!"
    return text
# AIzaSyAkZUo_b8eMR301uy2fPBLN4_gDV-tzAQ4
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
