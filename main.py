import requests
from pprint import pprint

API_Key ="666296dadbdc5a514e738a918ca52aee"

city = input("Enter your city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)

## Commentary
"""
Line 1&2:
    The required libraries needed for the implementation of this program are 
    imported before anything else. The 'requests' library allows us a user to 
    connect to a url and obtain data whereas the 'pprint' (PrettyPrinter) 
    library makes it easier to read the json file obtained via the API call.

Line 6:
    Here, a simple input statement collects information (city name) from the
    user to be used in the program. 
    
Line 7:
    The base_url variable holds the base link, concatenated with the API Key
    and the Query (user input). This is specially formatted based of the 
    documentation provided by Open Weather Map.

Line 8:
    The weather_data variable holds the output of the requests call on the 
    complete base_url in typical json format.

Line 9:
    The pprint library is implored here to convert the json out to human-readable
    tree format output. 
"""