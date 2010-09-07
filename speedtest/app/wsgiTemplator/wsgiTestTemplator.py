import os
from google.appengine.ext.webapp import util
from web import template

render = template.render('app/wsgiTemplator/templates')

class WSGITemplator:
  def __call__(self,environ,start_response):
    args = environ['PATH_INFO'].split("/")
    start_response("200 OK", [])
    return render.index(int(args[-2]),int(args[-1]))["__body__"]

app = WSGITemplator()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

