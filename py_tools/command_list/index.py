
#python3 index.py

import sys
import os 
import json


initJson = open('/Users/eason/tools/config/init.json') 
initJsonData = json.load(initJson)

print(initJsonData)
for key, value in initJsonData.items():
	# 去掉disabled
	if initJsonData[key].get("disabled") is None:
		print(key + ":" + str(value))

flag = True

while flag:
	choice = input()
	value = ""
	if choice.find("writesth") != -1 :
		value = choice[9:]
		choice = "writesth"
	
	command = {}
	try:
		command = initJsonData[choice]["cmd"]
	except:
		print("ERROR: {}".format(choice))
		continue

	if initJsonData[choice].get("chdir"):
		os.chdir(initJsonData[choice]["chdir"])
		flag = False

	elif choice.find("writesth") != -1 :
		command = command.format(value)

	
	if os.system(command) == 0:
		print("Success")
	else:
		print("FAIL! " + command)
		break

print("COMPLETE")
		
	# if os.system(initJsonData[choice]) == 0:
	# 	print("Success")
	# else:
	# 	print("Fail")