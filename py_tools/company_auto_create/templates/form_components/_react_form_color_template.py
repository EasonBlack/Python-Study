from jinja2 import Template

form_color_template =  Template('''
<Form.Item required label="{{title}}" 
	className={'align-items-center d-flex '}>
	<SketchPickerWrapper color={ d.{{props[0]}} || null} 
		selectColor = {(v) => onBasicChange("{{props[0]}}", v)} 
		hasHash={true} 
	/>
</Form.Item>
''')