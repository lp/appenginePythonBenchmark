import os, tenjin, tenjin.gae
from google.appengine.ext.webapp import util
from webob import Response, Request
from tenjin.helpers import *

tenjin.gae.init()

class WebObTenjinCache:
  def __call__(self,environ,start_response):
    args = Request(environ).path_info.split("/")
    context = { 'numA' : int(args[-2]), 'numB' : int(args[-1])}
    res = Response()
    res.body = tenjin.Engine(
      cache=tenjin.GaeMemcacheCacheStorage(),
      path=[os.path.join(os.path.dirname(__file__),"templates")]
      ).render('webobTenjinCacheTestTemplate.pyhtml',context)
    return res(environ,start_response)

app = WebObTenjinCache()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

