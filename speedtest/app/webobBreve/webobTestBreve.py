import os
from google.appengine.ext.webapp import util
from webob import Response, Request
from breve import Template
from breve.tags.html import tags

class WebObBreve:
  def __call__(self,environ,start_response):
    args = Request(environ).path_info.split("/")
    res = Response()
    bvars = dict ( numA = int(args[-2]), numB = int(args[-1]) )
    res.unicode_body = Template(tags,root=os.path.dirname(__file__)
      ).render('webobBreveTestTemplate',bvars)
    return res(environ,start_response)

app = WebObBreve()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

