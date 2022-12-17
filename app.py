from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_app():
    return '<h1>Agriculture Monitoring System</h1>'
    
@app.route('/sensor')
def my_app():
    return 'First Flask application!'
