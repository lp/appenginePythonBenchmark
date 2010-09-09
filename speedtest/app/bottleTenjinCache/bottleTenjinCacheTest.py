import os, bottle, tenjin, tenjin.gae
from bottle import get
from google.appengine.ext.webapp import util
from tenjin.helpers import *

bottle.debug(False)
app = bottle.default_app()
tenjin.gae.init()

@get('/bottletenjcache/:numA/:numB')
def index(numA,numB):
  context = { 'numA' : int(numA), 'numB' : int(numB)}
  return tenjin.Engine(
    cache=tenjin.GaeMemcacheCacheStorage(),
    path=[os.path.join(os.path.dirname(__file__),"templates")]
    ).render('bottleTenjinCacheTestTemplate.pyhtml',context)

def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()