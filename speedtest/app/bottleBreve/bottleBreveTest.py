import os, bottle
from bottle import get
from google.appengine.ext.webapp import util
from breve import Template
from breve.tags.html import tags

bottle.debug(False)
app = bottle.default_app()

@get('/bottlebreve/:numA/:numB')
def index(numA,numB):
  bvars = dict ( numA = int(numA), numB = int(numB) )
  return Template(tags,root=os.path.dirname(__file__)
    ).render('bottleBreveTestTemplate',bvars)

def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()