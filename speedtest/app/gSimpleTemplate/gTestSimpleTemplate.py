import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from bottle import template

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        self.response.out.write(template(
          os.path.join(os.path.dirname(__file__),'gTestTemplate.tpl'),
          numA=int(numA),numB=int(numB)))

application = webapp.WSGIApplication(
  [(r'/webappsimpletemplate/(.*)/(.*)', MainHandler)],debug=False)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()