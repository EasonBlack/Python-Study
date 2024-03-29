from jinja2 import Template

form_textarea_template =  Template('''
<Form.Item label="{{title}}"  className='align-items-center d-flex'>
		<Input className='w-250px' type='textarea'
			autosize={% raw %}{{ minRows: 4, maxRows: 4 }}{% endraw %}
			value={d.{{props[0]}}} onChange={this.onBasicChange.bind(this, '{{props[0]}}')}></Input>
	</Form.Item>

''')