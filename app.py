from flask import Flask, render_template, request, redirect, url_for
from models import User

app = Flask(__name__)

# Set up MongoDB connection
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

#select db
db = client['wadhw2']

#select collection 
users_collection = db['users']

# Define routes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # authentification
        user = User.find_by_username(username)
        if user and user.password == password:  
            return redirect(url_for('profile', username=username))
        else:
            return 'Invalid username or password'
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/logout')
def logout():
   
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
