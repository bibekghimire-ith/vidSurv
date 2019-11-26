from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


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

@app.route('/')
@app.route('/home')
@app.route('/dashboard')
def home():
    if not session.get('logged_in'):
        return login()
    else:
        return render_template('video.html')

@app.route('/controls')
def control():
    if not session.get('logged_in'):
        return login()
    else:
        return render_template('video001.html')


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


@app.route("/video")
def video():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:

        return render_template('videos.html')



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
