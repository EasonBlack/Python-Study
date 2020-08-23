from jinja2 import Template

form_checkBoxGroup_template =  Template('''
<Form.Item label="" labelWidth="200px" className='d-flex-column'>
	<Checkbox.Group value={d.{{props[0]}}} onChange={this.onBasicChange.bind(this, "{{props[0]}}")}>
		{
			this.props.{{title}}.map(p => {
				return <Checkbox label={p.value} key={p.value} trueLabel={p.text} falseLabel={p.text}></Checkbox>
			})
		}
	</Checkbox.Group>
</Form.Item>
''')