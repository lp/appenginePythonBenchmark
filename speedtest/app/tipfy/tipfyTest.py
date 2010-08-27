import tipfy
from tipfy import RequestHandler, Rule
from tipfy.ext.jinja2 import render_response, default_config

default_config['templates_dir']='app/tipfy/templates'

class TipfyBenchmarkHandler(RequestHandler):
    def get(self,numA,numB):
        return render_response('tipfyJinjaTestTemplate.html', nums=range(numA),numB=numB)

app = tipfy.Tipfy(rules=[Rule('/tipfyjinja/<int:numA>/<int:numB>', endpoint='tipfy', handler=TipfyBenchmarkHandler)])
def main():
    app.run()
    
if __name__ == '__main__':
    main()