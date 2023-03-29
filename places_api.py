import geopy as geopy
from googleplaces import GooglePlaces, types, lang, GooglePlacesError

YOUR_API_KEY = 'AIzaSyC4ncrcthGOoVjm9iXhQyyQ_mWxcxQyQ74'

google_places = GooglePlaces(YOUR_API_KEY)

user_location = input("Enter city: ")

# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
    radius=200, types=[types.TYPE_POLICE])
# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:
# http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

police_stations = []

for place in query_result.places:
    geo_loc = (place.geo_location['lat'], place.geo_location['lng'])
    place_distance = geopy.distance.distance(user_location, geo_loc).miles

    if place_distance <= 200:
        police_stations.append({
            'name': place.name,
            'location': geo_loc,
            'place_id': place.place_id,
            'details': place.details,
            'local_phone_number': place.local_phone_number,
            'website': place.website,
            'url': place.url,
            'distance_from_user_location': place_distance
        })

if query_result.has_attributions:
    print(query_result.html_attributions)

for place in query_result.places:
    # Returned places from a query are place summaries.
    print(place.name)
    print(place.geo_loc)
    print(place.place_id)

    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    print(place.details)  # A dict matching the JSON response from Google.
    print(place.local_phone_number)
    print(place.website)
    print(place.url)

    # Getting place photos

    for photo in place.photos:
        # 'maxheight' or 'maxwidth' is required
        photo.get(maxheight=500, maxwidth=500)
        # MIME-type, e.g. 'image/jpeg'
        photo.mimetype
        # Image URL
        photo.url
        # Original filename (optional)
        photo.filename
        # Raw image data
        photo.data

# Are there any additional pages of results?
if query_result.has_next_page_token:
    query_result_next_page = google_places.nearby_search(
        pagetoken=query_result.next_page_token)

# Adding and deleting a place
try:
    added_place = google_places.add_place(name='Mom and Pop local store',
                                          lat_lng={'lat': 51.501984, 'lng': -0.141792},
                                          accuracy=100,
                                          types=types.TYPE_HOME_GOODS_STORE,
                                          language=lang.ENGLISH_GREAT_BRITAIN)
    print(added_place.place_id)  # The Google Places identifier - Important!
    print(added_place.id)

    # Delete the place that you've just added.
    google_places.delete_place(added_place.place_id)
except GooglePlacesError as error_detail:
    # You've passed in parameter values that the Places API doesn't like..
    print(error_detail)
