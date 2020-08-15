from jinja2 import Template

form_input_template =  Template('''
<Form.Item required label="{{title}}"  className={' align-items-center  d-flex '}>
	<Input className='w-400px' 
		value={d.{{props[0]}}} onChange={(v)=>onBasicChange("{{props[0]}}", v)}></Input>
</Form.Item>

''')