from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process_form():
    if len(request.form['name'])<1:
        flash('Name cannot be empty')
        return redirect('/')
    elif len(request.form['comment'])<1:
        flash('Comment cannot be empty')
        return redirect('/')
    elif len(comment)>120:
        flash('Comment cannot exceed 120 characters')
        return redirect('/')
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return render_template('/result.html',name=session['name'],location=session['location'],language=session['language'],comment=session['comment'])
app.run(debug=True)
