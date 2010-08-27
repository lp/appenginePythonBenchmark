import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
                                     
class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB):
        nums = []
        numB_i = int(numB)
        for i in range(int(numA)):
          rmult = i * numB_i
          nums.append(str(rmult))
        
        templateValues = {
          "nums" : nums,
          "numB" : numB
        }
        self.response.out.write(
          template.render(os.path.join(
            os.path.dirname(__file__),
              "gnativeTestTemplate.html"),templateValues))

application = webapp.WSGIApplication(
  [(r'/webappdjango/(.*)/(.*)', MainHandler)],debug=False)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()