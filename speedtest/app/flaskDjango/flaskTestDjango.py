import os
from google.appengine.ext.webapp import util
from flask import Flask
from google.appengine.ext.webapp import template

app = Flask(__name__)

@app.route("/flaskdjango/<numA>/<numB>")
def test(numA,numB):
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
      "flaskDjangoTestTemplate.html"),templateValues)
    
def main():
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()
