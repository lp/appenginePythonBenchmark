import os, bottle
from bottle import get, template
from google.appengine.ext.webapp import util

bottle.debug(False)  # comment when getting to prod
app = bottle.default_app()

@get('/bottlesimpletemplate/:numA/:numB')
def index(numA,numB):
  return template(os.path.join(os.path.dirname(__file__),'bottleTestTemplate.tpl'),numA=int(numA),numB=int(numB))
  

def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()