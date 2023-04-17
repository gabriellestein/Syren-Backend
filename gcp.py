from google.cloud import storage
import json
from places_api import get_locations

# credentials to get access google cloud storage
# write your key path in place of gcloud_private_key.json
storage_client = storage.Client.from_service_account_json('gcp_json/syren-location-bucket.json')

# write your bucket name in place of bucket1go
bucket_name = 'syren_location_data'
BUCKET = storage_client.get_bucket(bucket_name)

def create_json(json_object, filename='locations.json'):
    '''
    this function will create json object in
    google cloud storage
    '''
    # create a blob
    blob = BUCKET.blob(filename)
    # upload the blob 
    blob.upload_from_string(
        data= json.dumps(json_object),
        content_type='application/json'
        )
    result = filename + ' upload complete'
    return {'response' : result}


def get_json(filename='locations.json'):
    '''
    this function will get the json object from
    google cloud storage bucket
    '''
    # get the blob
    blob = BUCKET.get_blob(filename)
    # load blob using json
    file_data = json.loads(blob.download_as_string())
    return file_data
    
def last_update_datetime(filename='locations.json'):
    blob = BUCKET.get_blob(filename)
    return "Updated: {}".format(blob.updated)
