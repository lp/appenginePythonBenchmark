import os, bottle
from bottle import get
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

bottle.debug(False)
app = bottle.default_app()

@get('/bottledjango/:numA/:numB')
def index(numA,numB):
  nums = []
  numB_i = int(numB)
  for i in range(int(numA)):
    rmult = i * numB_i
    nums.append(str(rmult))
  
  templateValues = {
    "nums" : nums,
    "numB" : numB
  }
  return template.render(
    os.path.join(os.path.dirname(__file__),
      "bottleDjangoTestTemplate.html"),templateValues)

def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()