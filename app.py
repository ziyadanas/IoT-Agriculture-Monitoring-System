from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone
import time
import requests

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
	return "<h2>home page Jaunty Jaguar</h2>"

@app.route('/reading',methods = ['POST', 'GET'])
def reading():
	if request.method == 'POST':
		sm = request.form['sm']
		ldr = request.form['ldr']
		return render_template('sensor.html', sm=sm, ldr=sm)
		
if __name__ == "__main__":
    app.run(host='0.0.0.0')
