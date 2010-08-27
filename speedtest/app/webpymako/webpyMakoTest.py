import os
from google.appengine.ext.webapp import util
import web
from mako.template import Template

web.config.debug = False
urls = (
	'/webpymako/(.*)/(.*)',	'index'
)
app = web.application(urls, globals())

class index:
  def GET(self,numA,numB):
    return Template(filename=os.path.join(os.path.dirname(__file__),"webpyTestMakoTemplate.html")).render(numA=int(numA),numB=int(numB))
    
def main():
  util.run_wsgi_app(app.wsgifunc())

if __name__ == "__main__":
  main()
