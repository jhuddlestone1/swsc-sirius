import random

#havent set data but other things work
data1 = []
for y in range(6):
    z = round(41.316970+(0.070033)*(y+1),6)
    print(z)
    data1.append(str(z))

linuxTime = []
for x in range (1489968000000,1489968030000,5000):
    linuxTime.append(x)
print(len(linuxTime))
fulldate =["2017-03-20T00:00:00Z","2017-03-20T00:00:05Z","2017-03-20T00:00:10Z","2017-03-20T00:00:15Z","2017-03-20T00:00:20Z","2017-03-20T00:00:25Z"]
print(len(fulldate))
# {"value": "41.026263", "datetime": "2017-03-20T10:30:15Z", "time": 1490005815000},
outFile = open('code-hum-0000.txt', 'w')
for y in range(6):
    outFile.write("{\"value\": \""+str(data1[y])+"\", \"datetime\": \""+str(fulldate[y])+"\", \"time\": "+str(linuxTime[y])+"},")
outFile.close()

