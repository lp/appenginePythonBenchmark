import os, bottle
from bottle import get
from google.appengine.ext.webapp import util
from jinja2 import Environment, FileSystemLoader

bottle.debug(False)
app = bottle.default_app()

@get('/bottlejinja/:numA/:numB')
def index(numA,numB):
  return Environment(loader=FileSystemLoader(
              os.path.join(
                  os.path.dirname(__file__),"templates/"))).get_template(
                      "bottleJinjaTestTemplate.html").render(nums=range(int(numA)),numB=int(numB))

def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()