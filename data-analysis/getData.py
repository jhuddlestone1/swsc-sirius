import json

with open('data.json') as json_file:
    data_all = json.load(json_file)

def getSingleElem(time1,elem1):
    return data_all[time1][elem1]

def getElemArray(elem2):
    elemArray = []
    for ltime1 in data_all:    #ltime1 = linux time
        elemArray.append(data_all[ltime1][elem2]) 
    return elemArray

temp_array = getElemArray("temperature")
hum_array = getElemArray("humidity")
co2_array = getElemArray("co2")
key_array = []    #array storing all the linux time
for x in data_all:    
    key_array.append(x)

#find the missing data
temp = 1489968025000
missingDate = []
for ltiem2 in key_array:
    if ((int(ltiem2) - temp)>5000):
        missingDate.append(ltiem2)
        print(ltiem2)
    temp = int(ltiem2)
# print(key_array[0])
# print(data_all["1490011225000"]["datetime"])
print(len(data_all))
linuxTime = []
for x in range (1489968000000,1490054400000,5000):
    linuxTime.append(x)
# print(len(linuxTime))


