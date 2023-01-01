from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone
import time
import requests

if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{hostname}/{databasename}".format(
    username="mohdafiqazizi",
    password="saya0000",
    hostname="mohdafiqazizi.mysql.pythonanywhere-services.com",
    databasename="mohdafiqazizi$agriculture",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class data(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    ldr     = db.Column(db.String(100))
    Sm      = db.Column(db.String(100))
    t	    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self,ldr,sm,t):
    	self.ldr	= ldr
    	self.sm		= sm
    	self.t	    = t


@app.route('/')
def home():
	return "<h2>home page Jaunty Jaguar</h2>"

@app.route('/reading',methods = ['POST', 'GET'])
def reading():
	if request.method == 'POST':
		sm = request.form['sm']
		ldr = request.form['ldr']
		sensor = data(sm = request.form['sm'],ldr = request.form['ldr'] )
		db.session.add(sensor)
		db.session.commit()
		return render_template('sensor.html', sm=sm, ldr=sm)
