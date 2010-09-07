import os
from google.appengine.ext.webapp import util
from webob import Response, Request
from google.appengine.ext.webapp import template

class WebObDjango:
  def __call__(self,environ,start_response):
    args = Request(environ).path_info.split("/")
    
    nums = []
    numB_i = int(args[-1])
    for i in range(int(args[-2])):
      rmult = i * numB_i
      nums.append(str(rmult))

    templateValues = {
      "nums" : nums,
      "numB" : args[-1]
    }
    
    res = Response()
    res.body = template.render(
      os.path.join(os.path.dirname(__file__),
        "webobDjangoTestTemplate.html"),templateValues)
    return res(environ,start_response)

app = WebObDjango()
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()

