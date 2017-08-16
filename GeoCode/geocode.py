# Use Google Maps to convert a location into Latitute/Longitute coordinates

# Imports
import httplib2
import json

def getGeocodeLocation(city, country):
	'''Use the Google Maps API to get Lat & Long'''
	google_api_key = "AIzaSyBwOf28YDZKRpEyEdZLM5xLPPISYkc9ZuI"
	locationString = city + ",+" + country
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	
	return latitude, longitude

print(getGeocodeLocation("Tokyo", "Japan"))