from jinja2 import Template

react_table_col_template =  Template(''' 
cols: [
\t{% for (col) in entityParams %}{ label: "", prop: "{{col[2]}}"}{% if loop.last == false %},{% endif %}\n\t{% endfor %}
]
''')