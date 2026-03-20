from flask import Flask, render_template 
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

@app.route('/index')
def index():
    return render_template('index.html') # it will try to look it in folder templates

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True) 
    # debug = True will keep on adding chnages while running. 
    # It means we do not need to restart server again and again


    
