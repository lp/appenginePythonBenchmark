import os, tipfy
from tipfy import RequestHandler, Response, Rule
from google.appengine.ext.webapp import template

class TipfyMakoBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
      nums = []
      for i in range(numA):
        rmult = i * numB
        nums.append(str(rmult))

      templateValues = {
        "nums" : nums,
        "numB" : numB
      }
      return Response(template.render(
        os.path.join(os.path.dirname(__file__),
          "tipfyDjangoTestTemplate.html"),templateValues))

app = tipfy.Tipfy(rules=[Rule('/tipfydjango/<int:numA>/<int:numB>', endpoint='tipfy', handler=TipfyMakoBenchmarkHandler)])
def main():
    app.run()
    
if __name__ == '__main__':
    main()