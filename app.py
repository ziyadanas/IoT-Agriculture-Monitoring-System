from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('form.html')

@app.route('/sensor', methods = ['POST', 'GET'])
def sensor():
	if request.method == 'POST':
		sm = request.form.get('sm')
		ldr = request.form.get('ldr')
		return render_template('sensor.html', sm=sm, ldr=ldr)
		#return "success receive data"
#	else:
#		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(debug=True, host='0.0.0.0', port=port)
