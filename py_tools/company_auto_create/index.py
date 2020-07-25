
import re
from jinja2 import Template
from _service_template import *
from _controller_template import *

entity_template = Template('''
package entities
import java.sql.Timestamp
case class {{entityName}}(
	{% for (col) in entityParams %} {{col[2]}} : {{col[1]}} {% if loop.last == false %},{% endif %} {% endfor %}
) extends IdEntity {
}

implicit lazy val  {{entityName2}}Format: Format[{{entityName}}] = Json.format[{{entityName}}]
''')

table_template = Template('''
class {{tableClassName}}(tag: Tag) extends IdTable[{{entityName}}](tag, "{{tableName}}", "f_id") {
{%- for (col) in entityParams %}	def {{col[2]}} = column[{{col[1]}}]("{{col[0]}}")
{% endfor %}
	override def * = ({% for (col) in entityParams %} {{col[2]}}{% if loop.last == false %},{% endif %} {% endfor %}) <>
	({{entityName}}.tupled, {{entityName}}.unapply)
}
lazy val {{tableClassNames}} = TableQuery[{{tableClassName}}]

''')





tableName = ""
fCols = []
tableClassName = ""

# 读取txt文件
fi = open("a.txt", 'r+')
r = fi.readlines() 
for l in r:
	l =  l.replace("\r", "").replace("\n", "").strip()
	matchObj = re.match( r'\((.*)\)', l, re.M|re.I)   # 第一行括号表示表明
	if matchObj:
		tableName = matchObj.group(1)  
		namePiece= 	tableName.split("_")[1:]
		entityName = "".join([ x.capitalize() for x in namePiece ])
		entityName2 = namePiece[0] + "".join([ x.capitalize() for x in tableName.split("_")[2:] ])
		tableClassName = entityName + "Table"
		tableClassNames = namePiece[0] + "".join([ x.capitalize() for x in tableName.split("_")[2:] ]) + "Tables"
	else:
		colName = l.split(" ")[0]
		colType = l.split(" ")[1]
		colKey = ""
		if colName.index("f_") >= 0:
			colKey =  colName.split("_")[1] + "".join([ c.capitalize() for (i,c) in enumerate(colName.split("_")[2:])  ])
		else:
			colKey =  colName.split("_")[0] + "".join([ c.capitalize() for (i,c) in enumerate(colName.split("_")[1:])  ])
		fCols.append((colName,  colType,  colKey))
print(tableName)
print(fCols)
print(entityName)

entityResult = entity_template.render(entityName=entityName,entityParams=fCols, entityName2=entityName2 )
tableResult = table_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames)
serviceResult = service_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames, entityName2=entityName2)
controllerResult = controller_template.render(entityName=entityName, entityParams=fCols, tableName=tableName, tableClassName=tableClassName, tableClassNames=tableClassNames, entityName2=entityName2)


print(entityResult)
print(tableResult)
print(serviceResult)
print(controllerResult)


entity_file = open("dict/" + entityName + '.scala','w+')
entity_file.write(entityResult + tableResult )
entity_file.close()

service_file = open("dict/" + entityName + 'Service.scala','w+')
service_file.write(serviceResult)
service_file.close()

controller_file = open("dict/" + entityName + 'Controller.scala','w+')
controller_file.write(controllerResult)
controller_file.close()

