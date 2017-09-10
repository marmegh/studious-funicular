from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "ReturnToPoohCorner"
@app.route('/')
def index():
    if session.get('start') is None:
        session['gold'] = 0
        date = datetime.now()
        for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
            session[attr] = getattr(date, attr)
            if session[attr] < 10:
                session[attr] = '0' + str(session[attr])
        activity = '{}/{}/{} {}:{}:{} - Started playing...'.format(session['month'], session['day'], session['year'], session['hour'], session['minute'], session['second'])
        session['activity'] = [activity,]
    return render_template('index.html', length = len(session['activity']), activity=session['activity'], gold=session['gold'])
@app.route('/process_money', methods=['POST'])
def money():
    session['start'] = False
    test = request.form['action']
    print test
    if test == 'farm':
        temp = random.randint(10,20)
        print temp
        session['gold']+=temp
        print session['gold']
        date = datetime.now()
        for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
            session[attr] = getattr(date, attr)
            if session[attr] < 10:
                session[attr] = '0' + str(session[attr])
        activity = '{}/{}/{} {}:{}:{} - Earned {} gold farming'.format(session['month'], session['day'], session['year'], session['hour'], session['minute'], session['second'], temp)
        session['activity'].append(activity)
        session['activity_length'] = len(session['activity'])
    if test == 'cave':
        temp = random.randint(5,10)
        print temp
        session['gold']+=temp
        activity = '{}/{}/{} {}:{}:{} - Earned {} gold in the cave'.format(session['month'], session['day'], session['year'], session['hour'], session['minute'], session['second'], temp)
        session['activity'].append(activity)
        session['activity_length'] = len(session['activity'])
        print session['gold']
    if test == 'house':
        temp = random.randint(2,5)
        print temp
        session['gold']+=temp
        activity = '{}/{}/{} {}:{}:{} - Earned {} gold at a house. BnE???'.format(session['month'], session['day'], session['year'], session['hour'], session['minute'], session['second'], temp)
        session['activity'].append(activity)
        session['activity_length'] = len(session['activity'])
        print session['gold']
    if test == 'casino':
        temp = random.randint(0,50)
        chance = random.randint(0,1)
        print chance
        if chance >0:
            session['gold']+=temp
            print session['gold']
            activity = '{}/{}/{} {}:{}:{} - Won {} gold at the casino'.format(session['month'], session['day'], session['year'], session['hour'], session['minute'], session['second'], temp)
        else:
            session['gold']-=temp
            print session['gold']
            activity = '{}/{}/{} {}:{}:{} - Lost {} gold at the casino'.format(session['month'], session['day'], session['year'], session['hour'], session['minute'], session['second'], temp)
        session['activity'].append(activity)
        session['activity_length'] = len(session['activity'])
    return redirect('/')
@app.route('/clear', methods = ['POST'])
def clear():
    del session['start']
    return redirect('/')
app.run(debug=True)
