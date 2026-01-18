from flask import Flask     #- importing the Flask class from the flask module.

'''
It creates an instance of the Flask class
which will be your WSGI (Web server gateway interface)
'''

#WSGI application
app=Flask(__name__)    #- __name__ tells Flask where to look for resources (like templates, static files)

@app.route("/")
def welcome():
    return "Welcome to Flask Application hell"   #- when user visits root URL, this message will be displayed

@app.route("/index")
def index():
    return "This is index page of Flask Application"   #- when user visits /index URL, this message will be displayed

# entry point which runs the app
if __name__=="__main__":            # it is enty point of any .py file
    app.run(debug=True)          # runs the application with debug mode enabled to see updates without restarting server



# to run application, use the command: python app.py  in this file's directory