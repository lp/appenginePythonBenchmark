import os
import webapp2 as webapp
from bottle import template

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        self.response.out.write(template(
          os.path.join(os.path.dirname(__file__),'g2TestTemplate.tpl'),
          numA=int(numA),numB=int(numB)))

application = webapp.WSGIApplication(
  [(r'/web2simpletemplate/(.*)/(.*)', MainHandler)],debug=False)

def main():
    application.run()

if __name__ == '__main__':
    main()