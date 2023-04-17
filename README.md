# Syren Back End

## Description
ETL pipeline that makes specialized calls to Google Maps API to get specific emergency resources.

## Endpoints
### /
This is the main endpoint for the API. It displays the location data currently stored in the GCP bucket.

### /manual
This manually updates the location data in the bucket. This can take several minutes and will either display a success or error message when the json file uploads.

### /check_update
This will return the date and time the bucket was last updated.

### Scheduled Event
The bucket is scheduled to automatically update everyday at noon.


## Roadmap
* Want to add less localized data (meaning more than just Greenville NC)

## CI/CD
Every time a commit is made to main the project will be rebuilt and re-deployed on GCP.