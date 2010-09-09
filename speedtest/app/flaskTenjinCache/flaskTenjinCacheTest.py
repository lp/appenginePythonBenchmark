import os, tenjin, tenjin.gae
from google.appengine.ext.webapp import util
from flask import Flask
from tenjin.helpers import *

tenjin.gae.init()
app = Flask(__name__)

@app.route("/flasktenjcache/<numA>/<numB>")
def test(numA,numB):
    context = { 'numA' : int(numA), 'numB' : int(numB)}
    return tenjin.Engine(
      cache=tenjin.GaeMemcacheCacheStorage(),
      path=[os.path.join(os.path.dirname(__file__),"templates")]
      ).render('flaskTenjinCacheTestTemplate.pyhtml',context)
    
def main():
    util.run_wsgi_app(app)

if __name__ == "__main__":
    main()
