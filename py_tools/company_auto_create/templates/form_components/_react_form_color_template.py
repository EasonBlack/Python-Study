from jinja2 import Template

form_color_template =  Template('''
<Form.Item  label="{{title}}" 
	className={'align-items-center d-flex '}>
	<SketchPickerWrapper color={ d.{{props[0]}} || null} 
		selectColor = {this.onBasicChange.bind(this, "{{props[0]}}")} 
		hasHash={true} 
	/>
</Form.Item>
''')