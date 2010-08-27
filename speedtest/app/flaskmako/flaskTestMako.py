import os
from google.appengine.ext.webapp import util
from flask import Flask
from mako.template import Template

app = Flask(__name__)

@app.route("/flaskmako/<numA>/<numB>")
def test(numA,numB):
    return Template(filename=os.path.join(
      os.path.dirname(__file__),"flaskTestMakoTemplate.html")).render(numA=int(numA),numB=int(numB))
    
def main():
    util.run_wsgi_app(app)

if __name__ == "__main__":
    main()
