import re
import os 

file_name = raw_input('file: ')
print os.path.exists(file_name)
if not os.path.exists(file_name):
    exit()



req_file = open(file_name).read().decode("utf-8")
# \u4e00-\u9fff chinese
# \uff00-\uffef\u3000-\u303f chinese punctuation 
result =re.sub(ur'[\u4e00-\u9fff\uff00-\uffef\u3000-\u303f]+\n', '', req_file)
print result

result_file =  open('result.txt', 'w')  
result_file.write(result)