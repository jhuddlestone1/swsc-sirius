import json

with open('data.json') as json_file:
    data_all = json.load(json_file)

def getSingleElem(time1,elem1):
    return data_all[time1][elem1]

def getElemArray(elem2):
    elemArray = []
    for x in data_all:
        elemArray.append(data_all[x][elem2]) 
    return elemArray

temp_array = getElemArray("temperature")
hum_array = getElemArray("humidity")
co2_array = getElemArray("co2")
key_array = []
for x in data_all:    
    key_array.append(x)

print(getSingleElem(key_array[0],"temperature"))
print(temp_array[0])

