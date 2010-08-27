import os
from google.appengine.ext.webapp import util
import web
from jinja2 import Environment, FileSystemLoader

web.config.debug = False
urls = (
	'/webpyjinja/(.*)/(.*)',	'index'
)
app = web.application(urls, globals())

class index:
  def GET(self,numA,numB):
    return Environment(loader=FileSystemLoader(
                os.path.join(
                    os.path.dirname(__file__),"templates/"))).get_template(
                        "webpyJinjaTestTemplate.html").render(nums=range(int(numA)),numB=int(numB))

def main():
  util.run_wsgi_app(app.wsgifunc())

if __name__ == "__main__":
  main()
