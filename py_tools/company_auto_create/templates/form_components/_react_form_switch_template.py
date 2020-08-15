from jinja2 import Template

form_switch_template =  Template('''
<Form.Item label="{{title}}">
	<Switch
		onText=""
		offText=""
		value={d.{{props[0]}}}
		onChange={this.onBasicChange.bind(this, '{{props[0]}}')}
	/>
</Form.Item>
''')