from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
	return "<h2>home page Jaunty Jaguar</h2>"

@app.route('/reading',methods = ['POST', 'GET'])
def reading():
	if request.method == 'POST':
		sm = request.args.get['sm']
		ldr = request.args.get['ldr']
		return render_template('sensor.html', sm=sm, ldr=sm)
	else:
		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    app.run()
