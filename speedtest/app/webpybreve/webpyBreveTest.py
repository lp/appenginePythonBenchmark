import os
from google.appengine.ext.webapp import util
import web
from breve import Template
from breve.tags.html import tags

web.config.debug = False
urls = (
	'/webpybreve/(.*)/(.*)',	'index'
)
app = web.application(urls, globals())

class index:
  def GET(self,numA,numB):
    bvars = dict ( numA = int(numA), numB = int(numB) )
    return Template(tags,root=os.path.dirname(__file__)
      ).render('webpyBreveTestTemplate',bvars)

def main():
  util.run_wsgi_app(app.wsgifunc())

if __name__ == "__main__":
  main()
