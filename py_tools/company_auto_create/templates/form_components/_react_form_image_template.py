from jinja2 import Template

form_image_template =  Template('''
<Form.Item label="{{title}}"  className='align-items-center d-flex'>
	<div className='d-flex align-items-center '>
		<ImageDropZone fileKey="product" className=' w-80px dropzone-border justify-content-center '
			setImageValue={(v) => onBasicChange("{{props[0]}}", v)}
			src={d.{{props[0]}}}
		/>
	</div>
	<span className='input-note'>建议分辨率:</span>
</Form.Item>
''')