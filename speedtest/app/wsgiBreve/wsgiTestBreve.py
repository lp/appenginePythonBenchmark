import os
from google.appengine.ext.webapp import util
from breve import Template
from breve.tags.html import tags

class WSGIBreve:
  def __call__(self,environ,start_response):
    args = environ['PATH_INFO'].split("/")
    start_response("200 OK", [])
    bvars = dict ( numA = int(args[-2]), numB = int(args[-1]) )
    return Template(tags,root=os.path.dirname(__file__)
      ).render('wsgiBreveTestTemplate',bvars)

app = WSGIBreve()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

