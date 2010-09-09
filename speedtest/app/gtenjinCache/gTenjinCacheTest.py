import os, tenjin, tenjin.gae
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from tenjin.helpers import *

tenjin.gae.init()

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        context = { 'numA' : int(numA), 'numB' : int(numB)}
        self.response.out.write(tenjin.Engine(
          cache=tenjin.GaeMemcacheCacheStorage(),
          path=[os.path.join(os.path.dirname(__file__),"templates")]
        ).render('gTenjinCacheTestTemplate.pyhtml',context))

application = webapp.WSGIApplication(
  [(r'/webapptenjcache/(.*)/(.*)', MainHandler)],debug=False)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()