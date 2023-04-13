from flask import Flask
import os
from flask_apscheduler import APScheduler
from apscheduler.triggers.cron import CronTrigger
import places_api as places
import gcp

class Config:
    SCHEDULER_API_ENABLED = True
    
app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route("/")
def index():
    return gcp.get_json()

@scheduler.task(id="scheduled_update_json", trigger=CronTrigger.from_crontab("0 12 * * *"))
def sheduled_location_update():
    print(gcp.create_json(places.get_locations()))

@app.route("/manual")
def manual_location_update():
    return gcp.create_json(places.get_locations())

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
