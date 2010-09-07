import os
from google.appengine.ext.webapp import util
from webob import Response, Request
from jinja2 import Environment, FileSystemLoader

class WebObJinja:
  def __call__(self,environ,start_response):
    args = Request(environ).path_info.split("/")
    res = Response()
    res.unicode_body = Environment(loader=FileSystemLoader(
                os.path.join(
                    os.path.dirname(__file__),"templates/"))).get_template(
                        "webobJinjaTestTemplate.html").render(nums=range(int(args[-2])),numB=int(args[-1]))
    return res(environ,start_response)

app = WebObJinja()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

