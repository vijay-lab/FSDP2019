
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content


print (response.text)
print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))

for key, value in response.headers.items():
    print (key, ":" ,value , "\n")
   
print ("Content type: " + response.headers['content-type'])


# Content in binary form
print (type(response.content))

print ("Content or Response Body : " + str(response.content))


# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
jsondata = response.json()
# response has the original JSON String
# jsondata has the convert string in the python data type dictionary

print (str(type(jsondata)))

print (jsondata)

print (jsondata.keys())

print (jsondata.values())

print (len(jsondata.items()))

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
   
jsondata["main"]["temp"]

"""
    Latitude and Longitude
    Weather Condition
    Wind Speed
    Sunset Rise and Set timing
"""
