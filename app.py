from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask import jsonify
import requests
import json
import time
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        username = User.query.filter_by(name=name).first()

        if existing_user:
            return jsonify({'status': 'error', 'message': 'Email already exists. Please use a different email.'})
        elif username:
             return jsonify({'status': 'error', 'message': 'Name already exists. Please use a different Name.'})
        elif len(password)<6:
            return jsonify({'status': 'error', 'message': 'Password too short'})
        elif len(name)<5:
             return jsonify({'status': 'error', 'message': 'Name too short.'})
        else:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'User registered successfully!'})

    return render_template('register.html')



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/projecthomepage')
        else:
            return jsonify('Invalid Email Or Password!')

    return render_template('login.html')


@app.route('/projecthomepage')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('projecthomepage.html',user=user)
    return redirect('/login')
@app.route('/redirect/<page_name>')
def redirect_to_page(page_name):
    if page_name == 'projecthomepage':
        return render_template('projecthomepage.html')
    elif page_name == 'login':
        return render_template('login.html')
    elif page_name == 'suggestions':
       return render_template('suggestions.html')
    elif page_name == 'help2':
       return render_template('help2.html')
    elif page_name == 'crops':
        return render_template('crops.html')
    elif page_name == 'fieldmonitor':
        return render_template('fieldmonitor.html')
    elif page_name == 'hmt':
        return render_template('hmt.html')
    elif page_name == 'index11':
        return render_template('index11.html')
    elif page_name == 'fertilisers':
        return render_template('fertilisers.html')
    elif page_name == 'alert':
        return render_template('alert.html')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True) 