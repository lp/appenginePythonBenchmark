import os
import webapp2 as webapp
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
              "g2nativeTestTemplate.html"),templateValues))

application = webapp.WSGIApplication(
  [(r'/web2django/(.*)/(.*)', MainHandler)],debug=False)

def main():
    application.run()

if __name__ == '__main__':
    main()