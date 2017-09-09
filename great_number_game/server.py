from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "CakeByTheOcean"
@app.route('/')
def index():
    session['computer'] = random.randint(1,100)
    print session['computer']
    session['guess'] = False
    session['test'] = 'start'
    return render_template('index.html', test = session['test'])
@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print type(session['guess'])
    print session['guess']
    if session['guess'] > session['computer']:
        session['test'] = 'high'
    elif session['guess'] < session['computer']:
        session['test'] = 'low'
    elif session['guess'] == session['computer']:
        session['test'] = 'equal'
    return render_template('index.html', test = session['test'], computer = session['computer'], guess = session['guess'])
@app.route('/again', methods=['POST'])
def again():
    session['computer'] = random.randint(1,100)
    session['test'] = False
    return redirect('/')
app.run(debug=True)
