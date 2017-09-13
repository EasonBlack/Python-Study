import re
import os 
from jinja2 import Environment, FileSystemLoader

class myTag:
  def __init__(self, tag, indents, classes, params):
    self.tag  = tag
    self.indents = indents
    self.classes = classes
    self.params = params
  def __str__(self):
    return '%s : %s' % (self.indents , self.tag)

output = open('output.txt', 'w')
tags = []
reserveTags = ['div', 'span']
content = '''div.container.d-flex.box__3wrapper:title='Name':value
    div.row:title='Schoole' 
      div.col-2
        title.box:title='hello'
        description.box:desc='this is somthing'
    div.row:title='Age' '''

classRegex = re.compile(r"\.([\w-]*)")
tagRegex = re.compile(r"^([\s\t]*)([\w]+)")
paramRegex = re.compile(r"\:([\w]+)[=]?[\'\"]?([\w]*)[\'\"]?")

for line in content.split('\n'):
  tagRes = tagRegex.findall(line)
  classRes = classRegex.findall(line)
  paramRes = paramRegex.findall(line)
  indents = tagRes[0][0].__len__()
  tag = tagRes[0][1]
  _tag =  myTag(tag, indents, classRes, paramRes)
  tags.append(_tag)


previousIndents = []
for tag in tags:  
  _startTag  =  tag.indents * ' ' + '<%s class="%s">' % (tag.tag, ' '.join(tag.classes))
  if(previousIndents.__len__() and tag.indents<=previousIndents[-1][0] ):
    while ( tag.indents<=previousIndents[-1][0]):
      _last = previousIndents.pop()
      output.write(_last[0] * ' ' + '</%s>\n' % _last[1])   
  
  previousIndents.append([tag.indents, tag.tag])
  output.write(_startTag + '\n')
  print previousIndents

while ( previousIndents.__len__()):
  _last = previousIndents.pop()
  output.write(_last[0] * ' ' + '</%s>\n' % _last[1])   

# create file
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(PATH),
    trim_blocks=False)



if not os.path.exists('dist'):
    os.makedirs('dist')
for tag in tags:
  if(tag.tag not in reserveTags):
    output = open('dist/'+ tag.tag +'.vue', 'w')
    _props = [x[0] for x in tag.params]
    html = TEMPLATE_ENVIRONMENT.get_template('vueTemplate').render({'props': _props})
    output.write(html)





