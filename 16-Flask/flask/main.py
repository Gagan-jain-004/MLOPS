## Integrating Hrml with Flask

from flask import Flask,render_template     #- importing the Flask class from the flask module.

# render template is used to render HTML files written seperately
#  in templates folder



#WSGI application
app=Flask(__name__)    #- __name__ tells Flask where to look for resources (like templates, static files)

@app.route("/")
def welcome():
    return "<html><H1>Weelo</H1></html>"   #- when user visits root URL, this message will be displayed

@app.route("/index")
def index():
    return render_template('index.html')     # it will go to chk inside templates folder to see index.html 

@app.route('/about')
def about():
    return render_template('about.html')



# entry point which runs the app
if __name__=="__main__":            # it is enty point of any .py file
    app.run(debug=True)          # runs the application with debug mode enabled to see updates without restarting server



# to run application, use the command: python app.py  in this file's directory