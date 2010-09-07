import os, tenjin, tenjin.gae
import webapp2 as webapp
from tenjin.helpers import *

tenjin.gae.init()

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        context = { 'numA' : int(numA), 'numB' : int(numB)}
        self.response.out.write(tenjin.Engine(path=[
          os.path.join(os.path.dirname(__file__),"templates")]
          ).render('g2TenjinTestTemplate.pyhtml',context))

application = webapp.WSGIApplication(
  [(r'/web2tenjin/(.*)/(.*)', MainHandler)],debug=False)

def main():
    application.run()

if __name__ == '__main__':
    main()