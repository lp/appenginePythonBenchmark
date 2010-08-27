import os
from google.appengine.ext.webapp import util
import web
from google.appengine.ext.webapp import template

web.config.debug = False
urls = (
	'/webpydjango/(.*)/(.*)',	'index'
)
app = web.application(urls, globals())

class index:
  def GET(self,numA,numB):
    nums = []
    numB_i = int(numB)
    for i in range(int(numA)):
      rmult = i * numB_i
      nums.append(str(rmult))

    templateValues = {
      "nums" : nums,
      "numB" : numB
    }
    return template.render(
      os.path.join(os.path.dirname(__file__),
        "webpyDjangoTestTemplate.html"),templateValues)
    
def main():
  util.run_wsgi_app(app.wsgifunc())

if __name__ == "__main__":
  main()
