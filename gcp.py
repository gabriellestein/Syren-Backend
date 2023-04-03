from google.cloud import storage
import json

# credentials to get access google cloud storage
# write your key path in place of gcloud_private_key.json
storage_client = storage.Client.from_service_account_json('gcloud_private_key.json')

# write your bucket name in place of bucket1go
bucket_name = 'bucket1go'
BUCKET = storage_client.get_bucket(bucket_name)

def create_json(json_object, filename):
    '''
    this function will create json object in
    google cloud storage
    '''
    # create a blob
    blob = BUCKET.blob(filename)
    # upload the blob 
    blob.upload_from_string(
        data=json.dumps(json_object),
        content_type='application/json'
        )
    result = filename + ' upload complete'
    return {'response' : result}

# your object
json_object = {
    'Name': 'Anurag',
    'Age': '23'
}
# set the filename of your json object
filename = 'test.json'

# run the function and pass the json_object
print(create_json(json_object, filename))

def get_json(filename):
    '''
    this function will get the json object from
    google cloud storage bucket
    '''
    # get the blob
    blob = BUCKET.get_blob(filename)
    # load blob using json
    file_data = json.loads(blob.download_as_string())
    return file_data

# write the filenam which you want
filename = 'test.json'

# run the function and pass the filename which you want to get
print(get_json(filename))