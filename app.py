# app.py
from flask import Flask, render_template, request, redirect, url_for, session, abort, json
from datetime import datetime
from UserModel import db,User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists 
from sqlalchemy import func, exc

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for security

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db.init_app(app)

@app.route('/')
def index():
    if not database_exists('sqlite:///user.db'):
        db.create_all()
        
    return render_template('index.html')


@app.route('/login/', methods=['GET','POST'])
def login():
    if 'username' in session:
        return redirect(url_for('profile', username=session['username']))

    elif request.method == 'POST':
       user_name = request.form['username']
       pass_word = request.form['password']
       try:
           user = User.query.filter_by(username = user_name).first()
           if user.password != pass_word:
               print('Incorrect password')
               return redirect(url_for('login'))
           else:
            session['username'] = user_name
            return redirect(url_for('profile', username = user_name))
            
       except:
          print('Unable to retrieve username')
          return redirect(url_for('login'))
        
    else:
        return render_template('login.html', login_error=session.pop('login_error', None))

@app.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['username']
        pass_word = request.form['password']
        new_score = 0
        new_user = User(username=user_name, password=pass_word,score = new_score)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'There was an issue adding new user'
    else:
        return render_template('register.html', register_error=session.pop('register_error', None))
    
    
@app.route('/logout/')
def logout():
    if 'username' in session:
        session.clear()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
@app.route('/profile/<username>')
def profile(username = None):
    if username is None:
        abort(404)
        
    user = User.query.filter_by(username = username).first()
    
    return render_template('profile.html', username = username, score = user.score)

@app.route('/challenges/')
def challenges(username = None):
    return render_template('challenges.html', username=session['username'])

@app.route('/output/')
def output():
    result = request.args.get('result', '')
    
    if result == 'Correct':
        user = User.query.filter_by(username = session['username']).first()
        user.score = 1 + user.score
        db.session.commit()
    
    return render_template('output.html', result=result)

if __name__ == '__main__':
    app.run()
