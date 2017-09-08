from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count = session['count'])
@app.route('/plus_two', methods=['POST'])
def plus_two():
    session['count'] += 2
    return render_template('index.html', count = session['count'])
@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 1
    return render_template('index.html', count = session['count'])
app.run(debug=True)
