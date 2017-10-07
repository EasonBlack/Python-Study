

import psutil

pList = ['notepad++.exe']

matches = [x for x in psutil.pids() if psutil.Process(x).name() in  ','.join(pList) ]
print (matches)
for p in matches:
    proc = psutil.Process(p)
    proc.kill()

# for pros in psutil.process_iter():
#     pinfo = pros.as_dict(attrs=['pid', 'name'])
#     try:
#         if pList.index(pinfo['name']) >= 0:
#             pros.kill()
#     except:
#         print('not in')



