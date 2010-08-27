from google.appengine.ext.webapp import util
import web

web.config.debug = False
render = web.template.render('app/webpy/templates')
urls = (
	'/webpytemplator/(.*)/(.*)',	'index'
)
app = web.application(urls, globals())

class index:
  def GET(self,numA,numB):
    return render.index(int(numA),int(numB))
    
def main():
  util.run_wsgi_app(app.wsgifunc())

if __name__ == "__main__":
  main()
