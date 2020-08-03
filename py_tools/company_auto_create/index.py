
import re
import sys, getopt
from jinja2 import Template

from templates._service_template import *
from templates._controller_template import *
from templates._route_template import *
from templates._redux_action_template import *
from templates._redux_template import *
from templates._react_table_col_template import *
from templates._entity_template import *
from templates._table_template import *


actionType = "scala-file"
# print('参数列表:', str(sys.argv))
opts, args = getopt.getopt(sys.argv[1:],"t:")
for op , value in opts: 
	if op == "-t":
		actionType = value

print(actionType)






tableName = ""
fCols = []
tableClassName = ""

# 读取txt文件
fi = open("_entity.txt", 'r+')
r = fi.readlines() 
for l in r:
	l =  l.replace("\r", "").replace("\n", "").strip()
	matchObj = re.match( r'\((.*)\)', l, re.M|re.I)   # 第一行括号表示表明
	if matchObj:
		tableName = matchObj.group(1)  # t_product_record
		namePiece= 	tableName.split("_")[1:]     # [product,record]
		routeName = "-".join([x for x in namePiece])  # product-record
		reduxName = "_".join([x.upper() for x in namePiece])  # PRODUCT_RECORD
		entityName = "".join([ x.capitalize() for x in namePiece ])  # ProductRecord
		entityName2 = namePiece[0] + "".join([ x.capitalize() for x in tableName.split("_")[2:] ])  # productRecord
		tableClassName = entityName + "Table"    # ProductRecordTable
		tableClassNames = namePiece[0] + "".join([ x.capitalize() for x in tableName.split("_")[2:] ]) + "Tables"  # productRecordTables
	else:
		colName = l.split(" ")[0]
		colType = l.split(" ")[1]
		colKey = ""
		if colName.index("f_") >= 0:
			colKey =  colName.split("_")[1] + "".join([ c.capitalize() for (i,c) in enumerate(colName.split("_")[2:])  ])
		else:
			colKey =  colName.split("_")[0] + "".join([ c.capitalize() for (i,c) in enumerate(colName.split("_")[1:])  ])
		colKey =  colKey.replace("id", "Id")  # 一般情况id都是i大写
		fCols.append((colName,  colType,  colKey))




entityResult = entity_template.render(entityName=entityName,entityParams=fCols, entityName2=entityName2 )
tableResult = table_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames)
serviceResult = service_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames, entityName2=entityName2)
controllerResult = controller_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames, entityName2=entityName2)
routeResult = route_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames, entityName2=entityName2, routeName=routeName)
reduxActionResult = redux_action_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames, entityName2=entityName2, routeName=routeName, reduxName=reduxName)
reduxResult = redux_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames, entityName2=entityName2, routeName=routeName, reduxName=reduxName)
reduxTableColsResult = react_table_col_template.render(entityParams=fCols)


results = []
if actionType == "scala-file":
	results.extend([
		(entityResult, entityName + '.scala' ), 
		(tableResult,  'Tables.scala'),
		(serviceResult, entityName + 'Service.scala'), 
		(controllerResult, entityName + 'Controller.scala'), 
		(routeResult,  entityName + '.routes'), 
	])
elif actionType == "js-file":
	results.extend([
		(reduxActionResult, entityName + '.reduce.js'), 
		(reduxResult,  entityName + '.action.js'), 
		(reduxTableColsResult,  "reduct_table_col.js")
	])


for result, filename in results:
	f =  open("dict/" + filename,'w+')
	f.write(result)
	f.close()



