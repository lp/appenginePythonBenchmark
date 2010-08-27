import os, bottle
from bottle import get
from google.appengine.ext.webapp import util
from web import template

render = template.render('app/bottleTemplator/templates')
bottle.debug(False)
app = bottle.default_app()

@get('/bottletemplator/:numA/:numB')
def index(numA,numB):
  return render.index(int(numA),int(numB))["__body__"]

def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()