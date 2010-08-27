import os
from google.appengine.ext.webapp import util
from flask import Flask
from bottle import template

app = Flask(__name__)

@app.route("/flasksimpletemplate/<numA>/<numB>")
def test(numA,numB):
    return template(
      os.path.join(os.path.dirname(__file__),'flaskTestTemplate.tpl'),
      numA=int(numA),numB=int(numB))
    
def main():
    util.run_wsgi_app(app)

if __name__ == "__main__":
    main()
