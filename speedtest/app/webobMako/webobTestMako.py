import os
from google.appengine.ext.webapp import util
from webob import Response, Request
from mako.template import Template

class WebObMako:
  def __call__(self,environ,start_response):
    args = Request(environ).path_info.split("/")
    res = Response()
    res.body = Template(
      filename=os.path.join(
        os.path.dirname(__file__),
          "webopMakoTemplate.html")).render(numA=int(args[-2]),numB=int(args[-1]))
    return res(environ,start_response)

app = WebObMako()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

