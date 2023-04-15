import mock

from gcp import create_json


@mock.patch("storage.Client")
def test_upload(client):
    # run function just recording interaction trought mock
    create_json("")

    # assert bucket was called with the passed string
    bucket = client().get_bucket
    bucket.assert_called_with("bucket")

    # assert blob and upload were called with expected params
    blob = bucket().blob
    blob.assert_called_with("report")
    blob().upload_from_string.assert_called_with("")
