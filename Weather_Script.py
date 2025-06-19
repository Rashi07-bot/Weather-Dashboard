import requests 
import time 
import os 
import json 


API_KEY = "483f6a4a6d1d33e86e27166b8352c7f4"
city="London"
CACHE_FILE = "weather_data.json"
CACHE_EXPIRE = 30 * 60 


def check_expiry_time():
    if not os.path.exists(CACHE_FILE) :
        return False
    last_modified = os.path.getmtime(CACHE_FILE)
    return (time.time() - last_modified ) < CACHE_EXPIRE 
    

def get_weather_data() :
    url= f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200 :
        data = response.json()
        with open(CACHE_FILE,"w") as f:
            json.dump(data,f) 
            print("Dumped fresh data")
        return data 
    else :
        raise Exception("API_ERROR",response.status_code)
    

def load_data() :
    if check_expiry_time()  :
        with open(CACHE_FILE,"r") as f :
            print("Loading JSON data...")
            return json.load(f)
    else :
        get_weather_data() 
        
weather_data = load_data()
print(weather_data)

    

    


