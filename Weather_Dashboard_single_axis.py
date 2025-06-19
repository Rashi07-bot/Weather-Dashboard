import pandas as pd 
from matplotlib import pyplot as plt 
import json
from datetime import datetime

with open('weather_data.json','r') as f :
    data = json.load(f) 

# print(data)
timestamp=[]
humidity=[]
temperatures = []
for entry in data['list'] :
    # print(entry)
    timestamp.append(datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S'))
    temperatures.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])

 
    

plt.figure(figsize=(10,6))


plt.plot(timestamp , temperatures , label="Temperatures (°C)" , color="orange" , marker="o")

plt.plot(timestamp , humidity , label = "Humidity" , color="blue" , linestyle="--" ,marker="x" )



plt.xlabel("Timestamp")
plt.ylabel("Value")

plt.title(f"Weather Forecast for {data['city']['name']}")
plt.legend()
plt.tight_layout()





plt.show()

    
