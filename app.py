from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from datetime import datetime
from pytz import timezone
import time
import os

app = Flask(__name__, template_folder='templates')

sm	= 0
ldr	= 0
t	= 0

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
	id 	= db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String('255'))
	dat = db.relationship('data',backref='sensor', uselist=False)

class data(db.Model):
	__tablename__ = "data"
	id = db.Column(db.Integer, primary_key=True)
	t	= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	val = db.Column(db.Integer)
	sensor_id	= db.Column(db.Integer,db.ForeignKey('sensor.id'))

# Initialize DB manually--------------------------------------------
engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sa.inspect(engine)
if not inspector.has_table("users"):
	with app.app_context():
		db.drop_all()
		db.create_all()
		app.logger.info('Initialized the database!')
else:
	app.logger.info('Database already contains the users table.')

# Backend Web-------------------------------------------------------
@app.route('/')
def home():
	return '<h2>Jaunty Jaugar</h2>'

@app.route('/sensor', methods = ['POST', 'GET'])
def sensor():
	global sensor1
	global sensor2
	global data1
	sensor1	= sensor(name = 'Soil Moisture')
	sensor2	= sensor(name = 'Light Intensity')
	if request.method == 'POST':
		dat1	= data(
			t = datetime.now(tz=timezone('Asia/Kuala_Lumpur')),
			val = request.form.get('sm'),
			sensor_id = 1
		    )
		dat2	= data(
			t = datetime.now(tz=timezone('Asia/Kuala_Lumpur')),
			val = request.form.get('ldr'),
			sensor_id = 2
			)    
		db.session.add_all([sensor1, sensor2])
		db.session.add_all([dat1, dat2])
		db.session.commit()
	return render_template('sensor.html', sm=sm, ldr=ldr)
		
#	else:
#		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(host='0.0.0.0', port=port, debug=True)
