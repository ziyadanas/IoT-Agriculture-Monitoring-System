from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='templates')


@app.route('/',methods = ['POST', 'GET'])
def home():
	if request.method == 'POST':
		sm = request.args.get['sm']
		ldr = request.args.get['ldr']
		return render_template('sensor.html', sm=sm, ldr=ldr)
	else:
		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    app.run(host="https://agriculture-iot.onrender.com", port=80, debug=True)
