
from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

CLIENT_ID = 'GKK34CITFCBFKCVRDQPNEWRWMVKRJPH0ZVKUSYHNTF2TXYUY'
CLIENT_SECRET = '4GCFQKF4DBEKCIFDNUGQ2O3NPPTUFUY01ZSZA5TNSGBW1ZDY'

def findARestaurant(mealType, city, country):
	'''Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.'''
	latitude, longitude = getGeocodeLocation(city, country)

	# Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	url = ("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s,%s&query=%s&v=20170801&m=foursquare" % (CLIENT_ID, CLIENT_SECRET, latitude, longitude, mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])
	
	if result['response']['venues']:
		# Grab the first restaurant
		restaurant = result['response']['venues'][0]
		venue_id = restaurant['id'] 
		restaurant_name = restaurant['name']
		if restaurant['location']['address']:
			address = restaurant['location']['address']
		elif restaurant['location']['formattedAddress']:
			restaurant_address = restaurant['location']['address']
			address = ""
			for r_a in restaurant_address:
				address += r_a
				
		# Get a  300x300 picture of the restaurant using the venue_id
		url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % (venue_id, CLIENT_ID, CLIENT_SECRET))
		result = json.loads(h.request(url, 'GET')[1])
		
		# Grab the first image
		if result['response']['photos']['items']:
			firstpic = result['response']['photos']['items'][0]
			prefix = firstpic['prefix']
			suffix = firstpic['suffix']
			imageURL = prefix + "300x300" + suffix

		else:
			# If no image available, insert default image url
			imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
		# Return a dictionary containing the restaurant name, address, and image url
		restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
		print("Restaurant Name: %s" % restaurantInfo['name'])
		print("Restaurant Address: %s" % restaurantInfo['address'])
		print("Image: %s \n" % restaurantInfo['image'])

		return restaurantInfo
	
	else:
		print("No Restaurants Found for %s" % city)

		return


findARestaurant("Pizza", "Tokyo", "Japan")
findARestaurant("Tacos", "Jakarta", "Indonesia")
findARestaurant("Tapas", "Maputo", "Mozambique")
findARestaurant("Falafel", "Cairo", "Egypt")
findARestaurant("Spaghetti", "New Delhi", "India")
findARestaurant("Cappuccino", "Geneva", "Switzerland")
findARestaurant("Sushi", "Los Angeles", "California")
findARestaurant("Steak", "La Paz", "Bolivia")
findARestaurant("Gyros", "Sydney", "Australia")
