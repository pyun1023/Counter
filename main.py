from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] =0
    else
        session['count'] +=1
    return render_template('index.html', count=session['count'])

@app.route('/two')
def add_two():
    session['count'] +=1
    return redirect('/')

@app.route('/destroy_session')
def delete():
    session['count']=0
    return redirect('/')

app.run(debug=True)