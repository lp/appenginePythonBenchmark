import os, tipfy
from tipfy import RequestHandler, Response, Rule
from breve import Template
from breve.tags.html import tags

class TipfyMakoBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
        bvars = dict ( numA = numA, numB = numB )
        return Response(
          Template(tags,root=os.path.dirname(__file__)
            ).render('tipfyBreveTestTemplate',bvars))

app = tipfy.Tipfy(rules=[
  Rule('/tipfybreve/<int:numA>/<int:numB>',
  endpoint='tipfy',
  handler=TipfyMakoBenchmarkHandler)
])

def main():
    app.run()
    
if __name__ == '__main__':
    main()