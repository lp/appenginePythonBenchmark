import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from jinja2 import Environment, FileSystemLoader

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB): 
        self.response.out.write(
            Environment(loader=FileSystemLoader(
                os.path.join(
                    os.path.dirname(__file__),"templates/"))).get_template(
                        "gjinjaTestTemplate.html").render(nums=range(int(numA)),numB=int(numB)))

application = webapp.WSGIApplication(
  [(r'/webappjinja/(.*)/(.*)', MainHandler)],debug=False)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()