from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from datetime import datetime
from pytz import timezone
import time
import os

app = Flask(__name__, template_folder='templates')

#PostgreSQL DB config----------------------------------------------
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{hostname}/{databasename}".format(
    username="agriculturedb_06pt_user",
    password="xWlYDxSmhulErXEGgNLF6M23fR1IYl0G",
    hostname="dpg-cepti91a6gdgsmcgg3c0-a.singapore-postgres.render.com",
    databasename="agriculturedb_06pt",
    )

"""
#external database
postgres://agriculturedb_06pt_user:xWlYDxSmhulErXEGgNLF6M23fR1IYl0G@dpg-cepti91a6gdgsmcgg3c0-a.singapore-postgres.render.com/agriculturedb_06pt

#internal database    
postgres://agriculturedb_06pt_user:xWlYDxSmhulErXEGgNLF6M23fR1IYl0G@dpg-cepti91a6gdgsmcgg3c0-a/agriculturedb_06pt
"""

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class sensor(db.Model):
    id		= db.Column(db.Integer, primary_key=True)
    name	= db.Column(db.String(50), default='Sensor')

class data(db.Model):
    id 	= db.Column(db.Integer, primary_key=True)
    val 	= db.Column(db.Integer)
    tstamp	= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Initialize DB manually--------------------------------------------
def recreate_db():
    db.drop_all()
    db.create_all()

# Backend Web-------------------------------------------------------
@app.route('/')
def home():
	return '<h2>Jaunty Jaugar</h2>'

@app.route('/read', methods = ['POST', 'GET'])
def read():
	global sm, ldr, t
	if request.method == 'POST':
		sm = request.form.get('s1')
		ldr = request.form.get('id')
		t	= datetime.now()
		dat = data(val=sm, tstamp=t)
		db.session.add(dat)
		db.session.commit()
	return '<h2>Sensor1	: {{sm}}%</h2><h2>ID	: {{ldr}}%</h2>'

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    recreate_db()
    app.run(host='0.0.0.0', port=port, debug=True)
