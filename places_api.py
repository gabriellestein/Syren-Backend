from googleplaces import GooglePlaces, types
import json

YOUR_API_KEY = 'AIzaSyAkZUo_b8eMR301uy2fPBLN4_gDV-tzAQ4'

google_places = GooglePlaces(YOUR_API_KEY)
attributions = ""
loc_dict = {}

class Place: 
    def __init__(self):
        self.name : str
        self.geo_location : str
        self.lat : str
        self.long : str
        self.place_id: str
        self.local_phone_number : str
        self.url: str
       
def near_search(loc, type="", keyword=""):
    # You may prefer to use the text_search API, instead.
    query_result = google_places.nearby_search(
        location= loc,
        # radius IN METERS SO CONVERT METERS TO MILES
        radius=16093.4, 
        type=type,
        keyword=keyword
        )
    add_loc_to_dict(query_result.places)
    
    while query_result.has_next_page_token:
        query_result = google_places.nearby_search(lat_lng={'lat':0, 'lng':0},pagetoken=query_result.next_page_token)
        add_loc_to_dict(query_result.places)
        
def add_loc_to_dict(places):
    for place in places:
        p = Place()
        p.name = place.name
        p.geo_location = str(place.geo_location)
        p.lat = str(place.geo_location['lat'])
        p.long = str(place.geo_location['lng'])
        p.place_id = place.place_id
        place.get_details()
        p.local_phone_number = place.local_phone_number
        p.url = place.url
        
        loc_dict[p.place_id] = {'name': p.name, 
                                'geo_location': p.geo_location, 
                                'phone': p.local_phone_number, 'url': p.url,
                                'place_id': p.place_id,
                                'lat': p.lat,
                                'long': p.long}

def near_search_all_locs():
    town = 'Greenville'
    state = 'NC'

    loc = f"{town}, {state}"
    near_search(loc, types.TYPE_HOSPITAL)
    near_search(loc, types.TYPE_POLICE)
    near_search(loc, types.TYPE_CHURCH)
    near_search(loc, types.TYPE_SYNAGOGUE)
    near_search(loc, types.TYPE_MOSQUE)
    near_search(loc, keyword='food bank')

def write_to_file():
    # TESTING FUNCTION
    near_search_all_locs()
    json_string=json.dumps(loc_dict)
    file=open("places.json","w")
    file2=open("places2.json","w", encoding="utf-8")
    json.dump(json_string,file)
    file2.write(str(loc_dict))
    file.close()
    file2.close()
    
def get_locations():
    near_search_all_locs()
    return json.dumps(loc_dict)