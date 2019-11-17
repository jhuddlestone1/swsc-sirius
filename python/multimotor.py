import RPi.GPIO as GPIO          
import sys
import time
from time import sleep
import json
import math

GPIO.setwarnings(False)

inputs = [23,24,14,8,20]
enabler = [25,15,7,21]

motor1 = [23,24]
motor2 = [23,14]
motor3 = [23,8]
motor4 = [23,20]

timeheight = 1489968030000
tempheight = 23.5
humheight = 36.0
co2height = 538.0

tempAvg = 23.2
humAvg = 36.0
co2Avg = 538.0

GPIO.setmode(GPIO.BCM)

for i in inputs:
    GPIO.setup(i,GPIO.OUT)

for e in enabler:
    GPIO.setup(e,GPIO.OUT)

for i in inputs:
    GPIO.output(i,GPIO.LOW)
    
p0=GPIO.PWM(enabler[0],500)
p1=GPIO.PWM(enabler[1],500)
p2=GPIO.PWM(enabler[2],500)
p3=GPIO.PWM(enabler[3],500)

p0.start(100)
p1.start(100)
p2.start(100)
p3.start(100)

def setup():
    forward(motor2, 10)
    forward(motor3, 10)
    forward(motor4, 10)

def forward(m, t):
    print("forward")
    GPIO.output(m[0],GPIO.HIGH)
    GPIO.output(m[1],GPIO.LOW)
    time.sleep(abs(t))
    stop(m)

def backward(m, t):
    print("backward")
    GPIO.output(m[0],GPIO.LOW)
    GPIO.output(m[1],GPIO.HIGH)
    time.sleep(abs(t))
    stop(m)
    
def stop(m):
    print("stop")
    GPIO.output(m[0],GPIO.LOW)
    GPIO.output(m[1],GPIO.LOW)

def m1Action(m, a, t):
    if a == 'f':
        forward(m, t)
    elif a =='b':
        backward(m, t)
    elif a == 's':
        stop(m)
    else:
        print("<<<  wrong data  >>>")
			
def m2Action(m, a, t):
    if a == 'f':
        forward(m, t)
    elif a =='b':
        backward(m, t)
    elif a == 's':
        stop(m)
    else:
        print("<<<  wrong data  >>>")

def m3Action(m, a, t):
    if a == 'f':
        forward(m, t)
    elif a =='b':
        backward(m, t)
    elif a == 's':
        stop(m)
    else:
        print("<<<  wrong data  >>>")
        
def m4Action(m, a, t):
    if a == 'f':
        forward(m, t)
    elif a =='b':
        backward(m, t)
    elif a == 's':
        stop(m)
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

# read file
with open('../data-analysis/data.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)

setup()

for key in obj:
    
    print(obj[key])
    
    timeVal = int(key)
    tempVal = int(obj[key]["temperature"])
    humVal = int(obj[key]["humidity"])
    co2Val = int(obj[key]["co2"])
    
    ############################
    
    t = (timeVal - timeheight) * 0.0002
    print(t)
    timeheight = timeVal
    if t > 0:
        m1Action(motor1, 'f', t)
    else:
        m1Action(motor1, 'b', t)
    
    ############################

    t = (tempVal - tempheight) * 10
    print(t)
    tempheight = tempVal
    if t > 0:
        m2Action(motor2, 'f', t)
    else:
        m2Action(motor2, 'b', t)
        
    #############################
        
    t = (humVal - humheight) * 5
    print(t)
    humheight = humVal
    if t > 0:
        m3Action(motor3, 'f', t)
    else:
        m3Action(motor3, 'b', t)
    
    #############################
    
    t = (co2Val - co2height) / 75
    print(t)
    co2height = co2Val
    if t > 0:
        m4Action(motor4, 'f', t)
    else:
        m4Action(motor4, 'b', t)

	
GPIO.cleanup()
