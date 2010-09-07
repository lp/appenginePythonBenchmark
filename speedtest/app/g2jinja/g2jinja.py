import os
import webapp2 as webapp
from jinja2 import Environment, FileSystemLoader

class MainHandler(webapp.RequestHandler):
    def get(self,numA,numB): 
        self.response.out.write(
            Environment(loader=FileSystemLoader(
                os.path.join(
                    os.path.dirname(__file__),"templates/"))).get_template(
                        "g2jinjaTestTemplate.html").render(nums=range(int(numA)),numB=int(numB)))

application = webapp.WSGIApplication(
  [(r'/web2jinja/(.*)/(.*)', MainHandler)],debug=False)

def main():
    application.run()

if __name__ == '__main__':
    main()