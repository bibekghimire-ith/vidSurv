#!/usr/bin/python3
from flask import Flask, render_template
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)

# Right  Motor
en1 = 32
R1 = 8  # Forward 
R2 = 10  # Reverse
gpio.setup(en1, gpio.OUT)
gpio.setup(R1, gpio.OUT)
gpio.setup(R2, gpio.OUT)
e1 = gpio.PWM(en1, 100)   # max-freq == 100

# Left Motor
en2 = 33
L1 = 36
L2 = 38
gpio.setup(en2, gpio.OUT)
gpio.setup(L1, gpio.OUT)
gpio.setup(L2, gpio.OUT)
e2 = gpio.PWM(en2, 100)

e1.start(100)
e2.start(100)

# Forward
def forward():
	e1.start(20)
	e2.start(20)
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.HIGH)
	gpio.output(R2, gpio.LOW)
	
	
# Bcakward
def backward():
	e1.start(20)
	e2.start(20)
	gpio.output(L2, gpio.HIGH)
	gpio.output(L1, gpio.LOW)
	gpio.output(R2, gpio.HIGH)
	gpio.output(R1, gpio.LOW)

	
# Turn Right
def turn_right():
	e1.start(20)
	e2.start(20)
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.LOW)
	gpio.output(R2, gpio.LOW)
	
	
# Turn Left
def turn_left():
	e1.start(20)
	e2.start(20)
	gpio.output(L1, gpio.LOW)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.HIGH)
	gpio.output(R2, gpio.LOW)
	
	
# Stop
def stop():
	e1.stop()
	e2.stop()
	gpio.output(L1, gpio.LOW)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.LOW)
	gpio.output(R2, gpio.LOW)


app = Flask(__name__)


def servo_Left():
    print('servo_Left')
def servo_Front():
    print('servo_Front')
def servo_Right():
    print('servo_Right')



@app.route('/')
@app.route('/home')
def index():
    return render_template('index2.html')

@app.route('/<device>/<action>')
def led(device, action):
    if device == 'servo' and action == 'left':
        servo_Left()
    if device == 'servo' and action == 'front':
        servo_Front()
    if device == 'servo' and action == 'right':
        servo_Right()



    if device == 'move' and action == 'forward':
        # forward()
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.HIGH)
	gpio.output(R2, gpio.LOW)

    if device == 'move' and action == 'left':
        # turn_left()
	gpio.output(L1, gpio.LOW)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.HIGH)
	gpio.output(R2, gpio.LOW)

    if device == 'move' and action == 'stop':
        # stop()
	gpio.output(L1, gpio.LOW)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.LOW)
	gpio.output(R2, gpio.LOW)

    if device == 'move' and action == 'right':
        # turn_right()
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.LOW)
	gpio.output(R2, gpio.LOW)

    if device == 'move' and action == 'backward':
        # backward()
	gpio.output(L2, gpio.HIGH)
	gpio.output(L1, gpio.LOW)
	gpio.output(R2, gpio.HIGH)
	gpio.output(R1, gpio.LOW)

    return 'true'

gpio.cleanup()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
    # app.run(debug=True)


