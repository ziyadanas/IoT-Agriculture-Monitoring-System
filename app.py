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
    __tablename__ = "data"
    id 	= db.Column(db.Integer, primary_key=True)
    val	= db.Column(db.Integer)
    dat = db.relationship('data',backref='sensor', uselist=False)

class data(db.Model):
    __tablename__ = "datasensor"
    id 	= db.Column(db.Integer, primary_key=True)
    t	= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sensor_id	= db.Column(db.Integer,db.ForeignKey('sensor.id'),nullable=False)

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
	global sm
	global ldr
	global t
	if request.method == 'POST':
		sm	= sensor(id = 1, val = request.form.get('sm'))
		ldr	= sensor(id = 2, val = request.form.get('ldr'))
		t	= data(t = datetime.now(tz=timezone('Asia/Kuala_Lumpur')), sensor = sensor)
		db.session.add(t)
		db.session.add(sm)
		db.session.add(ldr)
		db.session.commit()
	return render_template('sensor.html', sm=sm, ldr=ldr)
		
#	else:
#		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(host='0.0.0.0', port=port, debug=True)
