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

class Sensor(db.Model):
	__tablename__ = 'sensor'
	id		= db.Column(db.Integer, primary_key=True, unique = True)
	name	= db.Column(db.String(50), nullable=False, default = 'Unknown Sensor')
	data	= db.relationship('Data', back_populates='sensor')

class Data(db.Model):
	__tablename__ = 'data'
	id 			= db.Column(db.Integer, primary_key=True)
	timestamp	= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	sm			= db.Column(db.Integer)
	ldr			= db.Column(db.Integer)
	sensor_id	= db.Column(db.Integer,db.ForeignKey('sensor.id'))
	sensor		= db.relationship('Sensor', back_populates='data')

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

esp8266 = Sensor(id=1, name='NodeMCU ESP8266')
esp32	= Sensor(id=2, name='NodeMCU ESP32')
arduino	= Sensor(id=3, name='Arduino')
others	= Sensor(id=4, name='others')
db.session.add_all([esp8266, esp32, arduino, others])
db.session.commit()

# Backend Web-------------------------------------------------------
@app.route('/')
def home():
	return '<h2>Jaunty Jaugar</h2>'

@app.route('/sensor', methods = ['POST', 'GET'])
def sensor():
	global sm
	global ldr
	global data
	global sensor_id
	global timestamp
	if request.method == 'POST':
		timestamp	= datetime.now(tz=timezone('Asia/Kuala_Lumpur'))
		sm			= request.form.get('sm')
		ldr			= request.form.get('ldr')
		sensor_id	= request.form.get('id')
		data = Data(timestamp=timestamp, sm=sm, ldr=ldr, sensor_id=sensor_id) 
		db.session.add(data)
		db.session.commit()
	return render_template('sensor.html', sm=sm, ldr=ldr)
		
#	else:
#		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(host='0.0.0.0', port=port, debug=True)
