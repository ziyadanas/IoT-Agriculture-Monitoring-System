from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as create_engine
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
	name	= db.Column(db.Integer)

class data(db.Model):
	__tablename__ = "data"
	id			= db.Column(db.Integer, primary_key=True)
	val			= db.Column(db.Integer)
	timestamp	= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Initialize DB manually--------------------------------------------
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db.drop_all(engine)
db.create_all(engine)
app.logger.info('Initialized the database!')

# Backend Web-------------------------------------------------------
@app.route('/')
def home():
	return '<h2>Jaunty Jaugar</h2>'

@app.route('/data', methods = ['POST', 'GET'])
def data():
	global s1,timestamp
	if request.method == 'POST':
		s1			= request.form.get('sm')
		timestamp	= datetime.now(tz=timezone('Asia/Kuala_Lumpur'))
		dat			= data(val=s1, timestamp=timestamp)
		db.session.add(dat)
		db.session.commit()
	return render_template('data.html', s1=s1)
		
#	else:
#		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(host='0.0.0.0', port=port, debug=True)
