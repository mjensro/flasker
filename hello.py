from flask import Flask, render_template
#cd /c/flasker
#source virt/Scripts/activate to activate virtual env

#create flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
def index():
    return render_template("index.html")

#http://127.0.0.1:5000/student/Michelle
@app.route('/student/<name>')
def student(name):
    return render_template("user.html", user_name=name) #passing name from def
    #return "<h1>Welcome {}!</h1>".format(name)

#error page- invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#error page- internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


#{{}} used for variables
#{% for _ in _   %} logic(for/if statements)
#{% endfor %}
''' delete these if theres an issue
safe
capitalize
lower
upper
title
trim
striptags
'''