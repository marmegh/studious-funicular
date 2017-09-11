from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'IWishIKnewYou'
@app.route('/')
def index():
    session['fname'] = 'First Name'
    session['lname'] = 'Last Name'
    session['email'] = 'Email'
    session['testy'] = False
    return render_template('index.html', fname = session['fname'], lname = session['lname'], email = session['email'], test = session['testy'])
@app.route('/process', methods=['POST'])
def process():
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirmpw'] = request.form['confirmpw']
    session['testy'] = True
    session['verify'] = True
    if len(request.form['fname']) < 1:
        session['verify'] = False
        flash('First Name required')
    if len(request.form['lname']) < 1:
        session['verify'] = False
        flash('Last Name required')
    if len(request.form['email']) < 1:
        session['verify'] = False
        flash('Email required')
    if len(request.form['password']) < 1:
        session['verify'] = False
        flash('Password required')
    if request.form['password'] != request.form['confirmpw']:
        session['verify'] = False
        flash('Password and confirmation must match')
    if session['verify'] == False:
            return redirect('/')
    return render_template('success.html')
app.run(debug=True)
