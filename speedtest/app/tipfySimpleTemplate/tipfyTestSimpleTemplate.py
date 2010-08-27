import os, tipfy
from tipfy import RequestHandler, Response, Rule
from bottle import template

class TipfyMakoBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
        return Response(template(
          os.path.join(os.path.dirname(__file__),'tipfyTestTemplate.tpl'),
          numA=numA,numB=numB))

app = tipfy.Tipfy(
  rules=[Rule('/tipfysimpletemplate/<int:numA>/<int:numB>',
  endpoint='tipfy', handler=TipfyMakoBenchmarkHandler)]
)

def main():
    app.run()
    
if __name__ == '__main__':
    main()