# building url dynamically
# Variable Rule
# JINJA 2 template Engine

#Jinja 2 template Engine
'''
There are multiple ways to read the data source from the backened in the HTML source

1. {{}} to print output in HTML
2. {%...%} conditions, for loops
3. {#...#} this is for comments

'''

from flask import Flask, render_template, request, redirect, url_for 
#render_template will be used to redirect it to html page

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) Application
'''
#WSGI Application

app = Flask(__name__)

@app.route('/')
def Welcome():
    return '<html><h1> Welcome to my the Flask </h1></html>'

@app.route('/index',methods=['GET']) #if you do not use any method, default method is GET
def index():
    return render_template('index.html') # it will try to look it in folder templates

@app.route('/about')
def about():
    return render_template('about.html')


#variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >=50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score >=50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {'score':score, "res": res}
    return render_template('result1.html', results=exp)


@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('successres', score = total_score))


if __name__ =="__main__":
    app.run(debug=True) 
    # debug = True will keep on adding chnages while running. 
    # It means we do not need to restart server again and again


    
