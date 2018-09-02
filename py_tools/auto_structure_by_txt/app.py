import re
import shutil,os



file_name = input('Structure File Name: ')
my_file = open(file_name)
lines = my_file.readlines()



tabRegex =re.compile(r"(\s{2,4})")
templateRegex = re.compile(r"\[(\S+)\]")
root = './dist'
templateFolder = './templates'
current = './dist'
currentParent = ''
currentTab = 0

if os.path.exists(root):
    shutil.rmtree(root,ignore_errors=True ) 
os.makedirs(root)


for line in lines:
    length=len(tabRegex.findall(line))
    lineTemp = templateRegex.findall(line)
    # print(lineTem)
    line= line.replace('\n', '').replace(' ', '')

    if line == '':
        continue

    if length > currentTab:
        currentTab = length
        current = current + '\\' + currentParent
    elif length < currentTab:
        current = '\\'.join(current.split('\\')[0: (length - currentTab)])
        currentTab = length
      
    currentParent = line
    
    _target = ''.join([current,'\\',line])
    _target = templateRegex.sub('', _target)   # 去掉[]
    lineArr = line.split('.')
   
    if len(lineArr) > 1:       
        if len(lineTemp) >0:
            # print(_target, lineTemp[0], len(lineTemp))
            shutil.copyfile(templateFolder+"\\" + lineTemp[0], _target) 
        else:
            _file = open(_target,'w',encoding='utf8')
            _file.close()
    else:
        os.makedirs(_target)

    
