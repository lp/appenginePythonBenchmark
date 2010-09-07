import os
from google.appengine.ext.webapp import util
from mako.template import Template

class WSGIMako:
  def __call__(self,environ,start_response):
    args = environ['PATH_INFO'].split("/")
    start_response("200 OK", [])
    return Template(
      filename=os.path.join(
        os.path.dirname(__file__),
          "wsgiMakoTemplate.html")).render(numA=int(args[-2]),numB=int(args[-1]))

app = WSGIMako()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

