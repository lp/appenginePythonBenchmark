import os, web, tenjin, tenjin.gae
from google.appengine.ext.webapp import util
from tenjin.helpers import *

tenjin.gae.init()
web.config.debug = False
urls = (
	'/webpytenjin/(.*)/(.*)',	'index'
)
app = web.application(urls, globals())

class index:
  def GET(self,numA,numB):
    context = { 'numA' : int(numA), 'numB' : int(numB)}
    return tenjin.Engine(path=[
    os.path.join(os.path.dirname(__file__),"templates")]
      ).render('webpyTenjinTestTemplate.pyhtml',context)
    
def main():
  util.run_wsgi_app(app.wsgifunc())

if __name__ == "__main__":
  main()
