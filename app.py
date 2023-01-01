from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import requests
app = Flask(__name__,template_folder='templates')

url = "https://api.render.com/v1/services?limit=20"
headers = {"accept": "application/json","authorization": "Bearer rnd_nwKoQQOWPHs8Ap924QS19XVHx0ff"}

response = requests.get(url, headers=headers)

print(response.text)
    
@app.route('/',methods = ['POST', 'GET'])
def home():
	if request.method == 'POST':
		sm = request.args.get['sm']
		ldr = request.args.get['ldr']
		return render_template('sensor.html', sm=sm, ldr=ldr)
	else:
		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(debug=True, host='0.0.0.0', port=port) 
