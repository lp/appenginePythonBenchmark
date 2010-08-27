import os
from google.appengine.ext.webapp import util
from flask import Flask
from breve import Template
from breve.tags.html import tags

app = Flask(__name__)

@app.route("/flaskbreve/<numA>/<numB>")
def test(numA,numB):
    bvars = dict ( numA = int(numA), numB = int(numB) )
    return Template(tags,root=os.path.dirname(__file__)
      ).render('flaskBreveTestTemplate',bvars)
    
def main():
    util.run_wsgi_app(app)

if __name__ == "__main__":
    main()
