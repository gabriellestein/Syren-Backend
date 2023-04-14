import googlemaps
import json
import time

YOUR_API_KEY = 'AIzaSyAkZUo_b8eMR301uy2fPBLN4_gDV-tzAQ4'

gmaps = googlemaps.Client(key=YOUR_API_KEY)
loc_dict = {}

class Place: 
    def __init__(self):
        self.name : str
        self.geo_location : str
        self.lat : str
        self.long : str
        self.place_id: str
        self.types: str
        self.local_phone_number : str = ""
        self.url: str = ""
       
def near_search(loc, type=None, keyword=None):
    query_result = gmaps.places_nearby(location = loc, radius = 16063, type = type, keyword = keyword)
    add_loc_to_dict(query_result['results'])
    while 'next_page_token' in query_result.keys():
        time.sleep(10)
        query_result = gmaps.places_nearby(location = loc, radius = 16063, type = type, keyword = keyword, page_token=query_result['next_page_token'])
        add_loc_to_dict(query_result['results'])
    
        
def add_loc_to_dict(places):
    for place in places:
        p = Place()
        p.name = place['name']
        p.geo_location = str(place['geometry']['location'])
        p.lat = str(place['geometry']['location']['lat'])
        p.long = str(place['geometry']['location']['lng'])
        p.types = str(place['types'])
        p.place_id = place['place_id']
        details  = gmaps.place(place_id = p.place_id, fields=['formatted_phone_number', 'website'])['result']
        if 'formatted_phone_number' in details.keys():
            p.local_phone_number = details['formatted_phone_number']
        if 'website' in details.keys():
            p.url = details['website']
        
        loc_dict[p.place_id] = {'name': p.name, 
                                'geo_location': p.geo_location, 
                                'phone': p.local_phone_number, 'url': p.url,
                                'place_id': p.place_id,
                                'lat': p.lat,
                                'long': p.long,
                                'types': p.types}

def near_search_all_locs():
    town = 'Greenville'
    state = 'NC'

    loc = f"{town}, {state}"
    results = gmaps.geocode(loc)[0]
    loc = results['geometry']['location']
    near_search(loc, type='hospital')
    time.sleep(10)
    near_search(loc, type='police')
    time.sleep(10)
    near_search(loc, type='church')
    time.sleep(10)
    near_search(loc, type='synagogue')
    time.sleep(10)
    near_search(loc, type='mosque')
    time.sleep(10)
    near_search(loc, keyword='food bank')

def write_to_file():
    # TESTING FUNCTION
    get_locations()
    file2=open("places.json","w", encoding="utf-8")
    file2.write(json.dumps(loc_dict))
    file2.close()
    
def get_locations():
    near_search_all_locs()
    return json.dumps(loc_dict)
