import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from breve import Template
from breve.tags.html import tags

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        bvars = dict ( numA = int(numA), numB = int(numB) )
        self.response.out.write(
          Template(tags,root=os.path.dirname(__file__)
        ).render('gBreveTestTemplate',bvars))

application = webapp.WSGIApplication(
  [(r'/webappbreve/(.*)/(.*)', MainHandler)],debug=False)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()