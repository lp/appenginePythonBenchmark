import os, tenjin, tenjin.gae
from google.appengine.ext.webapp import util
from flask import Flask
from tenjin.helpers import *

tenjin.gae.init()
app = Flask(__name__)

@app.route("/flasktenjin/<numA>/<numB>")
def test(numA,numB):
    context = { 'numA' : int(numA), 'numB' : int(numB)}
    return tenjin.Engine(
      path=[os.path.join(os.path.dirname(__file__),"templates")]
      ).render('flaskTenjinTestTemplate.pyhtml',context)
    
def main():
    util.run_wsgi_app(app)

if __name__ == "__main__":
    main()
