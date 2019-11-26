#!/usr/bin/python3
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

# Right  Motor
en1 = 32
R1 = 24  # Forward 
R2 = 26  # Reverse
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
e1 = GPIO.PWM(en1, 100)   # max-freq == 100

# Left Motor
en2 = 33
L1 = 36
L2 = 38
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
e2 = GPIO.PWM(en2, 100)

e1.start(20)
e2.start(20)

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index2.html')

@app.route('/<device>/<action>')
def led(device, action):
	if device == 'move' and action == 'forward':
		GPIO.output(L1, GPIO.HIGH)
		GPIO.output(L2, GPIO.LOW)
		GPIO.output(R1, GPIO.HIGH)
		GPIO.output(R2, GPIO.LOW)
	if device == 'move' and action == 'backward':
		GPIO.output(L1, GPIO.LOW)
		GPIO.output(L2, GPIO.HIGH)
		GPIO.output(R1, GPIO.LOW)
		GPIO.output(R2, GPIO.HIGH)
	if device == 'move' and action == 'left':
		GPIO.output(L1, GPIO.LOW)
		GPIO.output(L2, GPIO.LOW)
		GPIO.output(R1, GPIO.HIGH)
		GPIO.output(R2, GPIO.LOW)
	if device == 'move' and action == 'right':
		GPIO.output(L1, GPIO.HIGH)
		GPIO.output(L2, GPIO.LOW)
		GPIO.output(R1, GPIO.LOW)
		GPIO.output(R2, GPIO.LOW)
	if device == 'move' and action == 'stop':
		GPIO.output(L1, GPIO.LOW)
		GPIO.output(L2, GPIO.LOW)
		GPIO.output(R1, GPIO.LOW)
		GPIO.output(R2, GPIO.LOW)

	return render_template('index2.html')

GPIO.cleanup()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(debug=True)







