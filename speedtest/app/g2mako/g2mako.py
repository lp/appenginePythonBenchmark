import os
import webapp2 as webapp
from mako.template import Template

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        self.response.out.write(
          Template(
            filename=os.path.join(
              os.path.dirname(__file__),
                "g2TestMakoTemplate.html")).render(numA=int(numA),numB=int(numB)))

application = webapp.WSGIApplication(
  [(r'/web2mako/(.*)/(.*)', MainHandler)],debug=False)

def main():
    application.run()

if __name__ == '__main__':
    main()