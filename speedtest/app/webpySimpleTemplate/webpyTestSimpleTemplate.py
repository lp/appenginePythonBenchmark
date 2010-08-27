import os
from google.appengine.ext.webapp import util
import web
from bottle import template

web.config.debug = False
urls = (
	'/webpysimpletemplate/(.*)/(.*)',	'index'
)
app = web.application(urls, globals())

class index:
  def GET(self,numA,numB):
    return template(
      os.path.join(os.path.dirname(__file__),'webpyTestTemplate.tpl'),
      numA=int(numA),numB=int(numB))
    
def main():
  util.run_wsgi_app(app.wsgifunc())

if __name__ == "__main__":
  main()
