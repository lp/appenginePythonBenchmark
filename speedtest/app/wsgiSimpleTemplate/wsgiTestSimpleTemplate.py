import os
from google.appengine.ext.webapp import util
from bottle import template

class WSGISimpleTemplate:
  def __call__(self,environ,start_response):
    args = environ['PATH_INFO'].split("/")
    start_response("200 OK", [])
    return template(
      os.path.join(os.path.dirname(__file__),'wsgiTestTemplate.tpl'),
      numA=int(args[-2]),numB=int(args[-1]))

app = WSGISimpleTemplate()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

