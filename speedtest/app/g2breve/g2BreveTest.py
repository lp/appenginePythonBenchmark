import os
import webapp2 as webapp
from breve import Template
from breve.tags.html import tags

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        bvars = dict ( numA = int(numA), numB = int(numB) )
        self.response.out.write(
          Template(tags,root=os.path.dirname(__file__)
        ).render('g2BreveTestTemplate',bvars))

application = webapp.WSGIApplication(
  [(r'/web2breve/(.*)/(.*)', MainHandler)],debug=False)

def main():
    application.run()

if __name__ == '__main__':
    main()