from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from googleplaces import GooglePlaces, types, lang
import sys, traceback


def hospitalLocationsOnCoordinates(locality):
    my_address = locality
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(my_address)
        # print(location.latitude, location.longitude)
        if location:
            hospitals = listOfHospitals(location)
            return hospitals
        else:
            return False
    except GeocoderTimedOut as e:
        print("Error: geocode failed on input %s with message %s" % (my_address, e.message))
        traceback.print_exc()
        return False


def listOfHospitals(location):
    API_KEY = 'AIzaSyCpqFrt7N_WWxSAOUVz-hm77R_ozQCXwgs'
    google_places = GooglePlaces(API_KEY)
    try:
        query_result = google_places.nearby_search(
            # lat_lng ={'lat': 46.1667, 'lng': -1.15},
            lat_lng={'lat': location.latitude, 'lng': location.longitude},
            radius=5000,
            # types =[types.TYPE_HOSPITAL] or
            # [types.TYPE_CAFE] or [type.TYPE_BAR]
            # or [type.TYPE_CASINO])
            types=[types.TYPE_HOSPITAL])
    except AttributeError as e:
        traceback.print_exc()
        return False

    if query_result.has_attributions:
        print(query_result.html_attributions)

        # Iterate over the search results
    i = 1
    listHospitals = []
    print("List of nearby hospitals: \n")
    for place in query_result.places:
        if i == 6:
            break
        # print(type(place))
        # place.get_details()
        listHospitals.append(str(i) + ". " + place.name)
        i = i + 1
    return listHospitals
