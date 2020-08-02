
from jinja2 import Template


table_template = Template('''
class {{tableClassName}}(tag: Tag) extends IdTable[{{entityName}}](tag, "{{tableName}}", "f_id") {
{% for (col) in entityParams %}\tdef {{col[2]}} = column[{{col[1]}}]("{{col[0]}}")
{% endfor %}
	override def * = ({% for (col) in entityParams %} {{col[2]}}{% if loop.last == false %},{% endif %} {% endfor %}) <>
	({{entityName}}.tupled, {{entityName}}.unapply)
}
lazy val {{tableClassNames}} = TableQuery[{{tableClassName}}]

''')