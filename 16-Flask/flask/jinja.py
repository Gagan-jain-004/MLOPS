# Jinja Templating 
'''
{{ }}  expression to print output in html
{% %}  statements like for loop, if condition
{# #}   comments in jinja template
'''



from flask import Flask,render_template,request,redirect,url_for     #- importing the Flask class from the flask module.

# render template is used to render HTML files written seperately
#  in templates folder



#WSGI application
app=Flask(__name__)    #- __name__ tells Flask where to look for resources (like templates, static files)

@app.route("/")
def welcome():
    return "<html><H1>Weelo</H1></html>"   #- when user visits root URL, this message will be displayed

@app.route("/index",methods=['GET'])         # by default it is get request if we dont write method=get
def index():
    return render_template('index.html')     # it will go to chk inside templates folder to see index.html 

@app.route('/about')
def about():
    return render_template('about.html')



# variable rule  - taking parameters from URL to use
'''
@app.route('/success/<int:score>')                # score parameter taken from URL
def success(score):
    return f'The score is '+ str(score)          # displaying the score passed in URL

    '''



## Building url dynamically 
@app.route('/success/<int:score>')                # score parameter taken from URL
def success(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    
    return render_template('result.html',result=res)   # passing result to result.html template



@app.route('/successres/<int:score>')                # score parameter taken from URL
def successres(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    
    exp={'score':score,'result':res}      # creating dictionary to pass multiple values to template
    
    return render_template('result1.html',result=exp)   # passing result to result1.html template



## if conditn
@app.route('/successif/<int:score>')                # score parameter taken from URL
def successif(score):
    
    return render_template('result.html',result=score)   # passing result to result.html template


@app.route('/fail/<int:score>')                # score parameter taken from URL
def fail(score):
       
    return render_template('result.html',result=score)   # passing result to result.html template

@app.route('/submit',methods=['POST','GET'])
def submit():
    totalscore=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])

        totalscore=(science+maths+c+datascience)/4
    else:
        return render_template('getresult.html')

    return redirect(url_for('successres',score=totalscore))


# entry point which runs the app
if __name__=="__main__":            # it is enty point of any .py file
    app.run(debug=True)          # runs the application with debug mode enabled to see updates without restarting server



# to run application, use the command: python jinja.py  in this file's directory