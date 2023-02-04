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

# Create DB with 1-to-1 relationship------------------------------
class sensor(db.Model):
	id	= db.Column(db.Integer, primary_key=True)
	nm	= db.Column(db.String(50), default='Sensor')
	data = db.relationship('data', back_populates='sensor', uselist=False)

class data(db.Model):
	id 	= db.Column(db.Integer, primary_key=True)
	tsp	= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	val	= db.Column(db.Integer)
	sid	= db.Column(db.Integer, db.ForeignKey('sensor.id'))
	sensor = db.relationship('sensor', back_populates='data', uselist=False)

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

@app.route('/register', methods = ['POST', 'GET'])
def register():
	if request.method == 'POST':
		nm = request.form.get('nm')
		id = request.form.get('id')
		dat	= sensor(id=id, nm=nm)
		db.session.add(dat)
		db.session.commit()
		return redirect('/read')
	return '''
		<form method="post">
			<p>Insert Device Name</p>
			<p><input type="text" name="nm" placeholder="name"></p>
			<p>Insert Device SID</p>
			<p><input type="text" name="id" placeholder="sid"></p>
			<p><input type="submit" value="Submit"></p>
		</form>
 	'''
"""
@app.route('/delete', methods=['GET', 'POST'])
def delete():
	if request.method == 'POST':
		nm	= request.form.get('nm')
		sid = request.form.get('id')
		ds 	= sensor.query.filter_by(id=sid).first()
		if not ds:
			return "Sensor with id {} not found".format(sid)
		db.session.delete(ds)
		db.session.commit()
		return "Sensor with id {} was deleted".format(sid)
	return '''
		<form method="post">
			<p>Insert Device Name</p>
			<p><input type="text" name="nm" placeholder="name"></p>
			<p>Insert Device SID</p>
			<p><input type="text" name="id" placeholder="sid"></p>
			<p><input type="submit" value="Delete"></p>
		</form>
	'''
"""
@app.route('/read', methods = ['POST', 'GET'])
def read():
	val	= request.form.get('s1')
	sid	= request.form.get('id')
	tsp	= datetime.now()
	html_string = """
	<html>
		<h2>Sensor1 : {}%</h2>
		<h2>ID : {}</h2>
	</html>
	""".format(val,sid)
	if request.method == 'POST':
		if not sid:
			return "<h2>Device is not assigned with ID</h2>"
		dat	= data(tsp=tsp, val=val, sid=sid)
		db.session.add(dat)
		db.session.commit()
		return html_string
	return html_string

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(host='0.0.0.0', port=port, debug=True)
