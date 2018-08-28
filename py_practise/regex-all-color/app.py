import re
import os 

folder_name = input('folder: ')
print(os.path.exists(folder_name))
if not os.path.exists(folder_name):
    exit()

arrFiles = []
for root, dirs, files in os.walk(folder_name):
    for f in files:
        arrFiles.append(root + "\\" + f)


print(arrFiles)

colorRegex = re.compile(r"(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})")
arrColor = []
for _file in arrFiles:  
    lines = open(_file).readlines()
    for line in lines:
        colorRes = colorRegex.findall(line)
        if(colorRes.__len__()):
            for colorSingle in colorRes: 
                if(colorSingle.split().__len__() > 1):
                    arrColor.extend(colorSingle.split())
                else:
                    arrColor.append(colorSingle)

print(arrColor)


