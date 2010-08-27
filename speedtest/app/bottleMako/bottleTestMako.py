import os, bottle
from bottle import get
from google.appengine.ext.webapp import util
from mako.template import Template

bottle.debug(False)
app = bottle.default_app()

@get('/bottlemako/:numA/:numB')
def index(numA,numB):
  return Template(
    filename=os.path.join(
      os.path.dirname(__file__),
        "bottleTestMakoTemplate.html")).render(numA=int(numA),numB=int(numB))

def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()