import os, tipfy
from tipfy import RequestHandler, Response, Rule
from web import template

render = template.render('app/tipfyTemplator/templates')

class TipfyMakoBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
        return Response(render.index(numA,numB)["__body__"])

app = tipfy.Tipfy(rules=[Rule('/tipfytemplator/<int:numA>/<int:numB>', endpoint='tipfy', handler=TipfyMakoBenchmarkHandler)])
def main():
    app.run()
    
if __name__ == '__main__':
    main()