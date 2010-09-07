import os
import webapp2 as webapp
from web import template

render = template.render('app/g2templator/templates')

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        self.response.out.write(
          render.index(int(numA),int(numB))["__body__"]
        )

application = webapp.WSGIApplication(
  [(r'/web2templator/(.*)/(.*)', MainHandler)],debug=False)

def main():
    application.run()

if __name__ == '__main__':
    main()