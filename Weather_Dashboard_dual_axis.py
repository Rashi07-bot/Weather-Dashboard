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
    
    
fig , ax1 = plt.subplots(figsize=(12,7))


ax1.plot(timestamp , temperatures , label="Temperatures (°C)" , color="orange" , marker="o")
ax1.set_xlabel("Timestamp")
ax1.set_ylabel("Temperatures")
ax1.tick_params(axis="y" , labelcolor = "orange")

ax2= ax1.twinx()

ax2.plot(timestamp , humidity , label = "Humidity" , color="blue" , linestyle="--" ,marker="x" )
ax2.set_ylabel("Humidity" , color='blue')
ax2.tick_params(axis="y" , labelcolor = "blue")




plt.title(f"Weather Forecast for {data['city']['name']}")
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))# plt.xticks(timestamp)
plt.tight_layout()
plt.show()

    
