import os
    
folderPath = "/Users/eason/Downloads/aa"
fileList=os.listdir(folderPath)


for i in fileList:
  _i = i.replace("_1.jpg", "")
  _i2 = _i.replace("_", "+")
  os.rename(os.path.join(folderPath,i),
    os.path.join(folderPath,  _i2)+".jpg")
 
  