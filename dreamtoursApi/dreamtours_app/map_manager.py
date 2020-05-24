from dreamtours_app import bbdd_manager
from dreamtours_app.models import Distance
import requests, json

def get_distance(origin, destination):
    return requests.get(ditancematrix_url + 'origins=' + origin +
                 '&destinations=' + destination +
                 '&key=' + api_key).json()

api_key = 'AIzaSyDZSCmTJ3jQLHwNol8t9a41hVXJb3V4Fy0'
ditancematrix_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

def serilize_distance(json):
    #id = bbdd_manager.get_last_distance_id()
    #print(json["destination_addresses"][0]+" "+json["origin_addresses"][0]+" "+json["rows"][0]["elements"][0]["distance"]["text"])
    #bbdd_manager.insert_distance(str(id), Distance("", json["destination_addresses"][0], json["origin_addresses"][0], json["rows"][0]["elements"][0]["distance"]["text"]))
    #distance = Distance(bbdd_manager.get_last_distance_id(), json["destination_addresses"][0], json["origin_addresses"][0], json["rows"][0]["elements"][0]["distance"]["text"])
    return Distance("", json["destination_addresses"][0], json["origin_addresses"][0], json["rows"][0]["elements"][0]["distance"]["text"])#id

#print(get_distance("Barcelona, Spain", "Madrid, Spain"))

