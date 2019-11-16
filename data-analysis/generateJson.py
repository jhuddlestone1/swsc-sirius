import json
import statistics 

with open('temp.json') as json_file:
    data_temp = json.load(json_file)

with open('humidity.json') as json_file:
    data_hum = json.load(json_file)

with open('CO2.json') as json_file:
    data_co2 = json.load(json_file)

write_data = {}
def writeJson(time1,date1,temp1,hum1,co21):
    write_data[time1] = []
    write_data[time1].append({
        'datetime': date1,
        'temperature': temp1,
        'humidity': hum1,
        'co2': co21
    })    

temp_temp = 10000000000000.00000000
temp_co2 = 10000000000000.00000000
for x in range (len(data_hum["values"])):
    for y in range(len(data_temp["values"])):
        if  (data_hum["values"][x]["time"] == data_temp["values"][y]["time"]):
            temp_temp = float(data_temp["values"][y]["value"])
            break

    for z in range(len(data_co2["values"])):
        if  (data_hum["values"][x]["time"] == data_co2["values"][z]["time"]):
            temp_co2 = float(data_co2["values"][z]["value"])
            break

    if (temp_co2 != 10000000000000.00000000 and temp_temp != 10000000000000.00000000):
        writeJson(data_hum["values"][x]["time"],data_hum["values"][x]["datetime"],temp_temp,float(data_hum["values"][x]["value"]),temp_co2)
    
    temp_temp = 10000000000000.00000000
    temp_co2 = 10000000000000.00000000

print(len(write_data))
with open('data1.txt', 'w') as outfile:
    json.dump(write_data, outfile)            #,indent=2)

