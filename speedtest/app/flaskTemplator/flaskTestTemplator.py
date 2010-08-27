import os
from google.appengine.ext.webapp import util
from flask import Flask
from web import template

render = template.render('app/flaskTemplator/templates')
app = Flask(__name__)

@app.route("/flasktemplator/<numA>/<numB>")
def test(numA,numB):
    return render.index(int(numA),int(numB))["__body__"]
    
def main():
    util.run_wsgi_app(app)

if __name__ == "__main__":
    main()
