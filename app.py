from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/')
def home():
	return render_template('login.html')
   
@app.route('/success/<name>')
def success(name):
	return render_template('index.html', p1=name)
   #return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      name = request.form['nm']
      pswd = request.form['pw']
      return redirect(url_for('success',name = name))
   else:
      username = request.args.get('nm')
      return redirect(url_for('success',name = name))

if __name__ == '__main__':
   app.run(debug = True)

