import os
from google.appengine.ext.webapp import util
from jinja2 import Environment, FileSystemLoader

class WSGIJinja:
  def __call__(self,environ,start_response):
    args = environ['PATH_INFO'].split("/")
    start_response("200 OK", [])
    return Environment(loader=FileSystemLoader(
                os.path.join(
                    os.path.dirname(__file__),"templates/"))).get_template(
                        "wsgiJinjaTestTemplate.html").render(nums=range(int(args[-2])),numB=int(args[-1]))

app = WSGIJinja()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

