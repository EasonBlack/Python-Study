from jinja2 import Template

form_daterange_template =  Template('''
<Form.Item label="{{title}}" className='align-items-center d-flex'>       
	<DateRanger className='date-item-editor mr-10'
			dateFrom={"{{props[0]}}"}
			dateTo={"{{props[1]}}"}
			isShowTime = {true}
			format="yyyy-MM-dd HH:mm:ss"
			setDateRange={this.onSetDateRange.bind(this)} />
</Form.Item>

{/* 
onSetDateRange(dateRange) {
	let df = new Date(moment(dateRange[0]).format("YYYY-MM-DD 00:00:00")).valueOf();
	let dt = new Date(moment(dateRange[1]).format("YYYY-MM-DD 23:59:59")).valueOf();
	let detail = Object.assign({}, this.props.detail);
	detail["startTime"] = df;
	detail["endTime"] = dt;
	this.props.actions.onStateChange("detail", detail)
}
*/}

''')