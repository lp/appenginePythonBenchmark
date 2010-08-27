from google.appengine.ext.webapp import util
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/flaskjinja/<numA>/<numB>")
def test(numA,numB):
    return render_template('flaskTestTemplate.html', nums=range(int(numA)),numB=int(numB))
    
def main():
    util.run_wsgi_app(app)

if __name__ == "__main__":
    main()
