from jinja2 import Template

form_input_template =  Template('''
<Form.Item  label="{{title}}"  className={' align-items-center  d-flex '}>
	<Input className='w-250px' 
		value={d.{{props[0]}}} onChange={this.onBasicChange.bind(this, "{{props[0]}}")}></Input>
</Form.Item>

''')