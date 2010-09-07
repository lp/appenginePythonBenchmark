import os, tenjin, tenjin.gae
from google.appengine.ext.webapp import util
from tenjin.helpers import *

tenjin.gae.init()

class WSGITenjin:
  def __call__(self,environ,start_response):
    args = environ['PATH_INFO'].split("/")
    start_response("200 OK", [])
    context = { 'numA' : int(args[-2]), 'numB' : int(args[-1])}
    return tenjin.Engine(
      path=[os.path.join(os.path.dirname(__file__),"templates")]
      ).render('wsgiTenjinTestTemplate.pyhtml',context)

app = WSGITenjin()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

