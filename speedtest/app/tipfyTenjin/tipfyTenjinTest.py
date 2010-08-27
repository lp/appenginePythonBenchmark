import os, tipfy, tenjin, tenjin.gae
from tipfy import RequestHandler, Response, Rule
from tenjin.helpers import *

tenjin.gae.init()

class TipfyTenjinBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
        context = { 'numA' : numA, 'numB' : numB}
        return Response(tenjin.Engine(
          path=[os.path.join(os.path.dirname(__file__),"templates")]
          ).render('tipfyTenjinTestTemplate.pyhtml',context))

app = tipfy.Tipfy(rules=[
  Rule('/tipfytenjin/<int:numA>/<int:numB>',
  endpoint='tipfy',
  handler=TipfyTenjinBenchmarkHandler)
])

def main():
    app.run()
    
if __name__ == '__main__':
    main()