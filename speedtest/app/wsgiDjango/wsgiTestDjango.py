import os
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class WSGIDjango:
  def __call__(self,environ,start_response):
    args = environ['PATH_INFO'].split("/")
    start_response("200 OK", [])
    nums = []
    numB_i = int(args[-1])
    for i in range(int(args[-2])):
      rmult = i * numB_i
      nums.append(str(rmult))

    templateValues = {
      "nums" : nums,
      "numB" : args[-1]
    }
    return template.render(
      os.path.join(os.path.dirname(__file__),
        "wsgiDjangoTestTemplate.html"),templateValues)

app = WSGIDjango()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

