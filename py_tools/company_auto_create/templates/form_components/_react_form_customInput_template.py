from jinja2 import Template

form_customInput_template =  Template('''
<Form.Item required className={' align-items-center  d-flex '}>
	{% for title in titles -%}
		{% if title != "input" -%}
			<span className='mr-10'>{{title}}</span> 
		{% else -%}
			<Input value={d.{{props[0]}}}  className="w-80px mr-10" onChange={this.onBasicChange.bind(this, "{{props[0]}}")}></Input>
		{% endif -%}
	{%- endfor %}
</Form.Item>
''')