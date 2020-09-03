from jinja2 import Template

form_branch_template =  Template('''
<Form.Item>
	<Button className='w-200px view-text mr-10 text-align-left border-radius-5'
		plain={true} type="info" onClick={this.toggleBranchSelect.bind(this)}>
		{getKeyTextByIds(d.branchIds || [], window.BRANCH_MAP, null, "门店")}
	</Button>
</Form.Item>

{/*
toggleBranchSelect() {
	this.setState({
		branchSelectorDisplay: !this.state.branchSelectorDisplay
	})
}
onBranchConfirm(v) {
	this.props.actions.onStateNestChange("detail", "branchIds", v)
	this.setState({
		branchSelectorDisplay: false
	})
}
*/}

{
	this.state.branchSelectorDisplay && <BranchSeletor
		dialogVisible={this.state.branchSelectorDisplay}
		filter={% raw %}{{ branchId: (detail && detail.branchIds) ? detail.branchIds.join(",") : "" }}{% endraw %}
		onCancel={this.toggleBranchSelect.bind(this)}
		onConfirm={this.onBranchConfirm.bind(this)}
	></BranchSeletor>
}
''')