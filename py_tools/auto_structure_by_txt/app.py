import re
import shutil,os



file_name = input('Structure File Name: ')
my_file = open(file_name)
lines = my_file.readlines()



tabRegex =re.compile(r"(\s{2,4})")
root = './dist'
current = './dist'
currentParent = ''
currentTab = 0

if os.path.exists(root):
    shutil.rmtree(root) 
os.makedirs(root)


for line in lines:
    length=len(tabRegex.findall(line))
    line= line.replace('\n', '').replace(' ', '')
    if length > currentTab:
        currentTab = length
        current = current + '\\' + currentParent
    elif length < currentTab:
        current = '\\'.join(current.split('\\')[0: (length - currentTab)])
        currentTab = length
      
    currentParent = line
    
    _target = ''.join([current,'\\',line])
    lineArr = line.split('.')
    if len(lineArr) > 1:
        # os.mknod(_target) 
        _file = open(_target,'w',encoding='utf8')
        _file.close()
    else:
        os.makedirs(_target)

    
