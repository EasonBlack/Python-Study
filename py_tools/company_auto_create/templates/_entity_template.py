
from jinja2 import Template


entity_template = Template('''
package entities
import java.sql.Timestamp
case class {{entityName}}(
	{% for (col) in entityParams %} {{col[2]}} : {{col[1]}} {% if loop.last == false %},{% endif %} {% endfor %}
) extends IdEntity {
}

implicit lazy val  {{entityName2}}Format: Format[{{entityName}}] = Json.format[{{entityName}}]
''')