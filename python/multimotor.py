import RPi.GPIO as GPIO          
import sys
import time
from time import sleep
import json

GPIO.setwarnings(False)

inputs = [23,24,14,8,20]
enabler = [25,15,7,21]

motor1 = [23,24]
motor2 = [23,14]
motor3 = [23,8]
motor4 = [23,20]

tempheight = 22.5
humheight = 27.0
co2height = 364.0
timeheight = 1489968030000

GPIO.setmode(GPIO.BCM)

for i in inputs:
    GPIO.setup(i,GPIO.OUT)

for e in enabler:
    GPIO.setup(e,GPIO.OUT)

for i in inputs:
    GPIO.output(i,GPIO.LOW)
    
p0=GPIO.PWM(enabler[0],1000)
p1=GPIO.PWM(enabler[1],1000)
p2=GPIO.PWM(enabler[2],1000)
p3=GPIO.PWM(enabler[3],1000)

p0.start(75)
p1.start(75)
p2.start(75)
p3.start(75)

def forward(m, t):
    print("forward")
    GPIO.output(m[0],GPIO.HIGH)
    GPIO.output(m[1],GPIO.LOW)
    time.sleep(t)
    stop(m)

def backward(m, t):
    print("backward")
    GPIO.output(m[0],GPIO.LOW)
    GPIO.output(m[1],GPIO.HIGH)
    time.sleep(t)
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
with open('data.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)

while(1):
	
    m = input("Choose a motor: ")
    a = input("Choose an action: ")
    v = input("Value: ")
    
    if m == "m1":
        t = v - timeheight
        m1Action(motor1, a, t)
    elif m == "m2":
        t = v - tempheight * 16
        m2Action(motor2, a, t)
    elif m == "m3":
        t = v - humheight
        m3Action(motor3, a, t)
    elif m == "m4":
        t = v - co2height * 0.05
	
GPIO.cleanup()