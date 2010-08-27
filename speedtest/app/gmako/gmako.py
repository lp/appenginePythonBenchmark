import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from mako.template import Template

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        self.response.out.write(
          Template(
            filename=os.path.join(
              os.path.dirname(__file__),
                "gTestMakoTemplate.html")).render(numA=int(numA),numB=int(numB)))

application = webapp.WSGIApplication(
  [(r'/webappmako/(.*)/(.*)', MainHandler)],debug=False)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()