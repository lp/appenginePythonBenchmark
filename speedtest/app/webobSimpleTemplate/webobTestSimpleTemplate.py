import os
from google.appengine.ext.webapp import util
from webob import Response, Request
from bottle import template

class WebObSimpleTemplate:
  def __call__(self,environ,start_response):
    args = Request(environ).path_info.split("/")
    res = Response()
    res.unicode_body = template(
      os.path.join(os.path.dirname(__file__),'webobTestTemplate.tpl'),
      numA=int(args[-2]),numB=int(args[-1]))
    return res(environ,start_response)

app = WebObSimpleTemplate()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

