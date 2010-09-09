import os, tipfy, tenjin, tenjin.gae
from tipfy import RequestHandler, Response, Rule
from tenjin.helpers import *

tenjin.gae.init()

class TipfyTenjinCacheBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
        context = { 'numA' : numA, 'numB' : numB}
        return Response(tenjin.Engine(
          cache=tenjin.GaeMemcacheCacheStorage(),
          path=[os.path.join(os.path.dirname(__file__),"templates")]
        ).render('tipfyTenjinCacheTestTemplate.pyhtml',context))

app = tipfy.Tipfy(rules=[
  Rule('/tipfytenjcache/<int:numA>/<int:numB>',
  endpoint='tipfy',
  handler=TipfyTenjinCacheBenchmarkHandler)
])

def main():
    app.run()
    
if __name__ == '__main__':
    main()