#!/usr/bin/python3
from flask import Flask, render_template
import RPi.GPIO as gpio
import time
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from datetime import datetime
import wget
from flask_sqlalchemy import SQLAlchemy
import shutil


basedir = os.path.abspath(os.path.dirname('__path__'))


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#############################

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    def __init__(self, snapshot):
        self.name = snapshot

    def __repr__(self):
        return f"{self.id}. {self.name}"

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



# Forward
def forward():
	e1.start(100)
	e2.start(100)
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.HIGH)
	gpio.output(R2, gpio.LOW)


# Bcakward
def backward():
	e1.start(100)
	e2.start(100)
	gpio.output(L1, gpio.LOW)
	gpio.output(L2, gpio.HIGH)
	gpio.output(R1, gpio.LOW)
	gpio.output(R2, gpio.HIGH)


# Turn Right
def turn_right():
	e2.start(100)
	e1.stop(100)
	gpio.output(L1, gpio.HIGH)
	gpio.output(L2, gpio.LOW)
	gpio.output(R1, gpio.LOW)
	gpio.output(R2, gpio.LOW)


# Turn Left
def turn_left():
	e1.start(100)
	e2.stop(100)
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





def servo_Left():
    print('servo_Left')
def servo_Front():
    print('servo_Front')
def servo_Right():
    print('servo_Right')


@app.route('/')
@app.route('/home')
@app.route('/dashboard')
def home():
    if not session.get('logged_in'):
        return login()
    else:
        return render_template('video.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def inputPW():
    if request.form['password'] == '19319' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Unauthorized access denied...')
    return home()


@app.route("/view")
def view():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        images = Image.query.order_by(Image.id.desc()).all()
        return render_template('view3.html', images=images)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/<device>/<action>')
def led(device, action):
    if device == 'servo' and action == 'left':
        servo_Left()
    if device == 'servo' and action == 'front':
        servo_Front()
    if device == 'servo' and action == 'right':
        servo_Right()

    if device == 'move' and action == 'forward':
        forward()
    if device == 'move' and action == 'left':
        turn_left()
    if device == 'move' and action == 'stop':
        stop()
    if device == 'move' and action == 'right':
        turn_right()
    if device == 'move' and action == 'backward':
        backward()
    return render_template('video.html')

@app.route('/snapshot')
def snapshot():
	dt = datetime.now()
	data = dt.strftime("%d-%m-%Y %H-%M-%S")
	image = 'Snapshot'+data+'.jpeg'
	# cmd = f"wget http://169.254.142.233:8080/?action=snapshot -o output"+data+".jpg"
	# os.system(f"wget http://169.254.142.233:8080/?action=snapshot -o output"+str(data)+".jpg")
	image_url = "https://image.shutterstock.com/image-photo/colorful-flower-on-dark-tropical-260nw-721703848.jpg"

	# Downloading image
	local_image_filename = wget.download(image_url, image)

	basedir = os.path.abspath(os.path.dirname('__path__'))
	dest = os.path.join(basedir, 'static\\images')

	snap = Image(image)
	db.session.add(snap)
	db.session.commit()

	shutil.move(image, dest)



# gpio.cleanup()

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run(debug=True)
