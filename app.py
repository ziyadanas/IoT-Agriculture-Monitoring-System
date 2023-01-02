from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import requests
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
	return "<h2>This is Agriculture monitoring system</h2>"
		    
@app.route('/reading',methods = ['POST', 'GET'])
def reading():
	if request.method == 'POST':
		sm = request.get_json['sm']
		ldr = request.get_json['ldr']
		return render_template('sensor.html', sm=sm, ldr=ldr)
	else:
		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(debug=True, host='0.0.0.0', port=port) 
