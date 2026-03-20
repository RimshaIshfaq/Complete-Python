from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) Application
'''
#WSGI Application

app = Flask(__name__)

@app.route('/')
def Welcome():
    return 'Welcome to my the Flask'

@app.route('/index')
def index():
    return "Welcome to Index Page"

if __name__ =="__main__":
    app.run(debug=True) 
    # debug = True will keep on adding chnages while running. 
    # It means we do not need to restart server again and again


    
