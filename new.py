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


def forward():
	e1.start(100)
	e2.start(100)
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.HIGH)
	gpio.output(R2, gpio.LOW)

def backward():
	e1.start(100)
        e2.start(100)
	gpio.output(L2, gpio.HIGH)
        gpio.output(L1, gpio.LOW)
        gpio.output(R2, gpio.HIGH)
        gpio.output(R1, gpio.LOW)

def turn_left():
	e1.start(100)
        e2.start(100)
	gpio.output(L2, gpio.LOW)
        gpio.output(L1, gpio.LOW)
        gpio.output(R1, gpio.HIGH)
        gpio.output(R2, gpio.LOW)

def turn_right():
	e1.start(100)
        e2.start(100)
	gpio.output(L1, gpio.HIGH)
        gpio.output(L2, gpio.LOW)
        gpio.output(R1, gpio.LOW)
        gpio.output(R2, gpio.LOW)

def stop():
	e1.stop()
        e2.stop()
        gpio.output(L1, gpio.LOW)
        gpio.output(L2, gpio.LOW)
        gpio.output(R1, gpio.LOW)


# forward()
# time.sleep(5)
# backward()
# time.sleep(5)
# turn_left()
# time.sleep(5)
# turn_right()
# time.sleep(5)
# gpio.cleanup()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return render_template('index000.html')

@app.route('/move')
def move():
	forward()
	time.sleep(20)

@app.route('/<device>/<action>')
def led(device, action):
	if device == 'move' and action == 'forward':
		print('Forward')
		e1.start(100)
		e2.start(100)
	        gpio.output(R1, gpio.HIGH)
	        gpio.output(R2, gpio.LOW)
	        gpio.output(L1, gpio.HIGH)
       		gpio.output(L2, gpio.LOW)

	if device == 'move' and action == 'stop':
                print('Stop...')
                e1.stop()
                e2.stop()
                gpio.output(R1, gpio.LOW)
                gpio.output(R2, gpio.LOW)
                gpio.output(L1, gpio.LOW)
                gpio.output(L2, gpio.LOW)

	return render_template('index000.html')



if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8000)





