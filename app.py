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
	__tablename__ = "sensor"
	id		= db.Column(db.Integer, primary_key=True)
	name	= db.Column(db.String(50), default = 'sensor')

class data(db.Model):
	__tablename__ = "data"
	id			= db.Column(db.Integer, primary_key=True)
	value		= db.Column(db.Integer)
	timestamp	= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

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
	if request.method == 'POST':
		dat	= data(
		value = request.form.get('S1'),
		timestamp = datetime.now(tz=timezone('Asia/Kuala_Lumpur'))
		)
		db.session.add(dat)
		db.session.commit()
	return render_template('data.html', s1 = request.form.get('S1'))
		
#	else:
#		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    recreate_db()
    app.run(host='0.0.0.0', port=port, debug=True)
