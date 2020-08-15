from jinja2 import Template

form_daterange_template =  Template('''
<Form.Item label="{{title}}" className='align-items-center d-flex'>       
	<DateRanger className='date-item-editor mr-10'
			dateFrom={"{{props[0]}}"}
			dateTo={"{{props[1]}}"}
			isShowTime = {true}
			format="yyyy-MM-dd HH:mm:ss"
			setDateRange={(v)=>onSetDateRange(v)} />
</Form.Item>

''')