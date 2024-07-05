import time
import serial
import csv

# record start time
start = time.time()

arduinoData = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1)
dataList=[]
#while True:
for i in range(100):
	while (arduinoData.inWaiting()==0):
		pass
	dataPacket = arduinoData.readline().decode('utf-8').strip('\r\n')
	#dataPacket = str(dataPacket, 'utf-8')
	#dataPacket = dataPacket.strip('\r\n')
	#print(dataPacket)
	dataList.append(dataPacket)
	#print(type(dataPacket))
	#for j in range(len(dataPacket)-1):
	#	dataList.append(dataPacket[j])
print(len(dataList))

with open('characterizationData_positive.csv', 'a') as csvfile:
    dataWriter = csv.writer(csvfile)
    dataWriter.writerow(dataList)
    #csvfile.write('\n'.join(dataList))

# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("Time of execution: ", (end-start)*10**3/1000, "s")
