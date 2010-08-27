import os, tipfy
from tipfy import RequestHandler, Response, Rule
from mako.template import Template

class TipfyMakoBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
        return Response(
          Template(
            filename=os.path.join(
              os.path.dirname(__file__),
                "tipfyTestMakoTemplate.html")).render(numA=numA,numB=numB))

app = tipfy.Tipfy(rules=[Rule('/tipfymako/<int:numA>/<int:numB>', endpoint='tipfy', handler=TipfyMakoBenchmarkHandler)])
def main():
    app.run()
    
if __name__ == '__main__':
    main()