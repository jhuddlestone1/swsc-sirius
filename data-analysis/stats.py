import json
import statistics 

with open('temp.json') as json_file:
    data_temp = json.load(json_file)

temp_value = []
for x in range(len(data_temp["values"])):
    temp_value.append(float(data_temp["values"][x]["value"]))

print("Data in temp")
print ("Minimum in temp: ",min(temp_value))
print ("Maximum in temp: ",max(temp_value))
print ("Mode in temp: ",statistics.mode(temp_value))
print ("Median in temp: ",statistics.median(temp_value))
print ("Mean in temp: ",statistics.mean(temp_value))    
#temp.json min:22.570545 max:23.610909 mode: 23.374909 median:23.290303 mean:23.1946173734375    

with open('humidity.json') as json_file:
    data_hum = json.load(json_file)

hum_value = []
for x in range(len(data_hum["values"])):
    hum_value.append(float(data_hum["values"][x]["value"]))

print("Data in humidity")
print ("Minimum in humidity: ",min(hum_value))
print ("Maximum in humidity: ",max(hum_value))
print ("Mode in humidity: ",statistics.mode(hum_value))
print ("Median in humidity: ",statistics.median(hum_value))
print ("Mean in humidity: ",statistics.mean(hum_value))    
#humidity.json min:27.98 max:42.798485 mode:41.878687 median:38.766364 mean:36.17916742498231 
 
with open('CO2.json') as json_file:
    data_co2 = json.load(json_file)

co2_value = []
for x in range(len(data_co2["values"])):
    co2_value.append(float(data_co2["values"][x]["value"]))

print("Data in CO2")
print ("Minimum in CO2: ",min(co2_value))
print ("Maximum in CO2: ",max(co2_value))
print ("Mode in CO2: ",statistics.mode(co2_value))
print ("Median in CO2: ",statistics.median(co2_value))
print ("Mean in CO2: ",statistics.mean(co2_value))    
#CO2.json min:364.6 max:924.2 mode:407.733333 median:520.79596 mean:536.396427559716
