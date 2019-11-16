import RPi.GPIO as GPIO          
from time import sleep

inputs = [23,24,14,8,20]
enabler = [25,15,7,21]
temp1=1

m1 = [23,24]
m2 = [23,14]
m3 = [23,8]
m4 = [23,20]

GPIO.setmode(GPIO.BCM)

for i in inputs:
    GPIO.setup(x,GPIO.OUT)

for e in enabler:
    GPIO.setup(x,GPIO.OUT)

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

def forward():
    print("forward")
    GPIO.output(inputs[0],GPIO.HIGH)
    GPIO.output(inputs[1],GPIO.LOW)
    temp1=1
    action[0]='z'

def backward():
    print("backward")
    GPIO.output(inputs[0],GPIO.LOW)
    GPIO.output(inputs[1],GPIO.HIGH)
    temp1=0
    action[0]='z'
    
def stop():
    print("stop")
    GPIO.output(inputs[0],GPIO.LOW)
    GPIO.output(inputs[1],GPIO.LOW)
    action[0]='z'

def m1Action(action):
    p0.ChangeDutyCycle(action[1])
    if action[0] == 'f':
        forward(action[1])
    elif action[0] == 'b':
        backward(action[1])
    elif action[0] == 's':
        stop()
    elif a=='e':
        GPIO.cleanup()
        break
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
			
def m2Action(action):
    p1.ChangeDutyCycle(action[1])
    if action[0] == 'f':
        forward(action[1])
    elif action[0] == 'b':
        backward(action[1])
    elif action[0] == 's':
        stop()
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")	

def m3Action(action):
    p2.ChangeDutyCycle(action[1])
    if action[0] == 'f':
        forward(action[1])
    elif action[0] == 'b':
        backward(action[1])
    elif action[0] == 's':
        stop()
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
        
def m4Action(action):
    p3.ChangeDutyCycle(action[1])
    if action[0] == 'f':
        forward(action[1])
    elif action[0] =='b':
        backward(action[1])
    elif action[0] == 's':
        stop()
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

while(1):
	
    m = input("Choose a motor: ")
    a = input("Choose an action: ")
    s = input("Choose a speed: ")
    
    action = [a,s]
    
    if m == "m1":
        m1Action(action)
    elif m == "m2":
        m2Action(action)
	elif m == "m3":
        m2Action(action)
	elif m == "m4":
        m2Action(action)
    else:
        GPIO.cleanup()
        break
