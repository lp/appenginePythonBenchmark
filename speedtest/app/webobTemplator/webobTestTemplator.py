import os
from google.appengine.ext.webapp import util
from webob import Response, Request
from web import template

render = template.render('app/webobTemplator/templates')

class WebObTemplator:
  def __call__(self,environ,start_response):
    args = Request(environ).path_info.split("/")
    res = Response()
    res.unicode_body = render.index(int(args[-2]),int(args[-1]))["__body__"]
    return res(environ,start_response)

app = WebObTemplator()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

