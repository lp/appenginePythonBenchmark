import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from web import template

render = template.render('app/gtemplator/templates')

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        self.response.out.write(
          render.index(int(numA),int(numB))["__body__"]
        )

application = webapp.WSGIApplication(
  [(r'/webapptemplator/(.*)/(.*)', MainHandler)],debug=False)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()