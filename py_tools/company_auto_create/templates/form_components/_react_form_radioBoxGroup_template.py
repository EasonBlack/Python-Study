from jinja2 import Template

form_radioBoxGroup_template =  Template('''
<Form.Item label=""  className='d-flex-column' labelWidth="200px">
	{% for title in titles %}
	 <Radio value={ {{loop.index0}} } checked={d.{{props[0]}} ==  {{loop.index0}} } className=''
        onChange={this.onBasicChange.bind(this, "{{props[0]}}")}>{{title}}</Radio>
	{% endfor %}
</Form.Item>
''')