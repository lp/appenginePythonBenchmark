from web.template import CompiledTemplate, ForLoop, TemplateResult

_dummy = CompiledTemplate(lambda: None, 'dummy')
join_ = _dummy._join
escape_ = _dummy._escape

def index (numA,numB):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'<body>\n'])
    extend_([u'    <table>\n'])
    for i in loop.setup(range(numA)):
        extend_(['        ', u'<tr><td>', escape_(i, True), u'</td><td>x ', escape_(numB, True), u'</td><td>= ', escape_(( i * numB ), True), u'</td></tr>\n'])
    extend_([u'    </table>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

index = CompiledTemplate(index, 'app/bottleTemplator/templates/index.html')

