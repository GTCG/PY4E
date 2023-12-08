"""
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 6052 characters
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8
Turn In

Please run your program to find the place_id for this location:

Penn State University
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJkQJ ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.
"""

import urllib.request
import urllib.parse
import urllib.error
import json

serviceurl= "http://py4e-data.dr-chuck.net/json?"
api_key = 42

while True:
    address = input("Enter location: ")
    if len(address) < 1 :break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print ("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print ("Retrieved", len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print("=== Failure to retrieve ===")
        print(data)
        continue

    print (json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js["results"][0]["formatted_address"]
    placeID = js["results"][0]["place_id"]
    print ('lat: ', lat, 'lng: ', lng)
    print (location)
    print (placeID)
