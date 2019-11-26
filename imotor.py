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

e1.start(20)
e2.start(20)

def forward():
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.HIGH)
	gpio.output(R2, gpio.LOW)

def backward():
	gpio.output(L2, gpio.HIGH)
        gpio.output(L1, gpio.LOW)
        gpio.output(R2, gpio.HIGH)
        gpio.output(R1, gpio.LOW)

def turn_left():
	gpio.output(L2, gpio.LOW)
        gpio.output(L1, gpio.LOW)
        gpio.output(R1, gpio.HIGH)
        gpio.output(R2, gpio.LOW)

def turn_right():
	gpio.output(L1, gpio.HIGH)
        gpio.output(L2, gpio.LOW)
        gpio.output(R1, gpio.LOW)
        gpio.output(R2, gpio.LOW)


forward()
time.sleep(5)
backward()
time.sleep(5)
turn_left()
time.sleep(5)
turn_right()
time.sleep(5)
gpio.cleanup()







