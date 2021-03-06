from flask import Flask, render_template
import os

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/employees')
def employees():
    return render_template('screen.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/desktop-feed')
def desktop_feed():
    return render_template('desktop-feed.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/login')
def login():
    return render_template('login.html')

PORT = os.getenv('PORT')
if PORT is None:
    PORT = 8080
app.run(debug=True,host='0.0.0.0',port=int(PORT))