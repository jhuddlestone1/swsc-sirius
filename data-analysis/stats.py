import json
import statistics 
import numpy as np
import matplotlib.pyplot as plt

with open('temperature.json') as json_file:
    data_temp = json.load(json_file)

temp_value = []
for x in range(len(data_temp["values"])):
    temp_value.append(float(data_temp["values"][x]["value"]))

# plt.plot(temp_value);
print("Data in temp")
print ("Minimum in temp: ",min(temp_value))
print ("Maximum in temp: ",max(temp_value))
print ("Mode in temp: ",statistics.mode(temp_value))
print ("Median in temp: ",statistics.median(temp_value))
print ("Mean in temp: ",statistics.mean(temp_value))   
print ("var in temp: ",np.var(temp_value)) 
print ("SD in temp: ",np.std(temp_value))    
#temp.json min:22.570545 max:23.610909 mode: 23.374909 median:23.290303 mean:23.1946173734375 var:0.06081028271028037 SD temp:0.2465974101856716

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
print ("var in humidity: ",np.var(hum_value))   
print ("SD in humidity: ",np.std(hum_value)) 
#humidity.json min:27.98 max:42.798485 mode:41.878687 median:38.766414499999996 mean:36.17262533576389 var:21.624520573029205 SD:4.650217260841606
 
with open('CO2.json') as json_file:
    data_co2 = json.load(json_file)

co2_value = []
for x in range(len(data_co2["values"])):
    co2_value.append(float(data_co2["values"][x]["value"]))

# co2_time = []
# for a in range(len(data_co2["values"])):
#     co2_time.append(data_co2["values"][a]["datetime"])
# print(co2_time[1])
# for i in range(len(co2_time)):
#     for j in range(len(co2_time)):
#         if (co2_time[i] == co2_time[j]) and (i != j):
#             print(co2_time[i])
print("Data in CO2")
print ("Minimum in CO2: ",min(co2_value))
print ("Maximum in CO2: ",max(co2_value))
print ("Mode in CO2: ",statistics.mode(co2_value))
print ("Median in CO2: ",statistics.median(co2_value))
print ("Mean in CO2: ",statistics.mean(co2_value))    
print ("var in CO2: ",np.var(co2_value)) 
print ("SD in CO2: ",np.std(co2_value)) 
#CO2.json min:364.6 max:924.2 mode:407.733333 median:523.753535 mean:539.5172556848959  var: 19233.291242363237  SD:138.68414200031393

print("co2",len(co2_value))
print("hum",len(hum_value))
print("temp",len(temp_value))




###Get the datatime array
# datetime_value = []
# for x in range(len(data_temp["values"])):
#     datetime_value.append(data_temp["values"][x]["datetime"])

# print(data_temp["values"][12804]["datetime"])
# temp_datetime = []
# for a in range(12804,12964):
#     temp_datetime.append(data_temp["values"][a]["datetime"])
# print((temp_datetime))