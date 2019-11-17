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
date_array = getElemArray("datetime")

key_array = []    #array storing all the key (linux time)
for x in data_all:    
    key_array.append(x)

print("existing Length",len(key_array))
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
linuxTime = []    #all linux Time
for x in range (1489968000000,1490054400000,5000):
    linuxTime.append(str(x))
print("Full Length",len(linuxTime))
print("index",key_array.index("1490023030000"))
print(key_array[11006])
print(linuxTime[11006])

# missingDateFull = []
# for x in linuxTime:
#     try:
#         y = key_array.index(str(x))
#     except:
#         missingDateFull.append(x)
        

# print("Difference",len(missingDateFull))


