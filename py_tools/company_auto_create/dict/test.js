
render() {
	let { detail } = this.props;
	let { currentTab } = this.state;

	return <div className='h-100 d-flex-column'>
		<TopNav title="" url="" />
		<DetailTop />
		<Menu defaultActive={currentTab} className="tab-nav" mode="horizontal" onSelect={this.onSelect.bind(this)}>
			<Menu.Item index="basic">基本信息</Menu.Item>
		</Menu>
		<div className='p-20 flex-1 overflow-y-auto'>
			<Form
				model={detail}
				ref="form" labelPosition="left" labelWidth="100"
				className= {'demo-ruleForm ' +  classNames({hide: currentTab != "basic"})} >
				
		
				
				<FormPanelWapper title="信息">
					<React.Fragment>
					
						
							
<Form.Item  label="活动名称"  className={' align-items-center  d-flex '}>
	<Input className='w-400px' 
		value={d.name} onChange={this.onBasicChange.bind(this, "name")}></Input>
</Form.Item>

						
						
						
						
						
						
						
						
						
						
						
						
					
						
							
<Form.Item  label="副标题"  className={' align-items-center  d-flex '}>
	<Input className='w-400px' 
		value={d.subTitle} onChange={this.onBasicChange.bind(this, "subTitle")}></Input>
</Form.Item>

						
						
						
						
						
						
						
						
						
						
						
						
					
						
						
						
						
						
						
							
<Form.Item label="使用说明"  className='align-items-center'>
		<Input className='w-400px' type='textarea'
			autosize={{ minRows: 4, maxRows: 4 }}
			value={d.usageDesc} onChange={this.onBasicChange.bind(this, 'usageDesc')}></Input>
	</Form.Item>

						
						
						
						
						
						
						
					
						
						
						
						
							
<Form.Item label="ICON"  className='align-items-center d-flex'>
	<div className='d-flex align-items-center '>
		<ImageDropZone fileKey="product" className=' w-80px dropzone-border justify-content-center '
			setImageValue={this.onBasicChange.bind(this, "detailIcon")}
			src={d.detailIcon}
		/>
	</div>
	<span className='input-note'>建议分辨率:</span>
</Form.Item>
						
						
						
						
						
						
						
						
						
					
						
						
						
						
							
<Form.Item label="ICON"  className='align-items-center d-flex'>
	<div className='d-flex align-items-center '>
		<ImageDropZone fileKey="product" className=' w-80px dropzone-border justify-content-center '
			setImageValue={this.onBasicChange.bind(this, "previewIcon")}
			src={d.previewIcon}
		/>
	</div>
	<span className='input-note'>建议分辨率:</span>
</Form.Item>
						
						
						
						
						
						
						
						
						
					
						
						
						
						
						
						
						
						
						
						
						
						
					
					</React.Fragment>
				</FormPanelWapper>
				
<SeperateLine className='mb-20' />
				
				<FormPanelWapper title="时间">
					<React.Fragment>
					
						
						
							
<Form.Item label="起止时间" className='align-items-center d-flex'>       
	<DateRanger className='date-item-editor mr-10'
			dateFrom={"startTime"}
			dateTo={"endTime"}
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

						
						
						
						
						
						
						
						
						
						
						
					
						
						
						
						
						
						
						
						
						
						
						
						
					
					</React.Fragment>
				</FormPanelWapper>
				
<SeperateLine className='mb-20' />
				
				<FormPanelWapper title="规则">
					<React.Fragment>
					
						
						
						
						
						
						
						
						
						
						
						
						
					
					</React.Fragment>
				</FormPanelWapper>
				
<SeperateLine className='mb-20' />
				
				<FormPanelWapper title="奖励">
					<React.Fragment>
					
						
							
<Form.Item  label="消费订单满"  className={' align-items-center  d-flex '}>
	<Input className='w-400px' 
		value={d.convertVal} onChange={this.onBasicChange.bind(this, "convertVal")}></Input>
</Form.Item>

						
						
						
						
						
						
						
						
						
						
						
						
					
						
							
<Form.Item  label="订单金额满"  className={' align-items-center  d-flex '}>
	<Input className='w-400px' 
		value={d.convertAmount} onChange={this.onBasicChange.bind(this, "convertAmount")}></Input>
</Form.Item>

						
						
						
						
						
						
						
						
						
						
						
						
					
						
						
						
						
						
						
						
						
						
						
						
							

<Form.Item label=""  className='no-ml-form' >
   <React.Fragment>
			<div className=' d-flex'><div className='w-150px'>优惠券</div><div className='w-150px'>数量</div>
				<div className='w-100px'></div>
			</div>
      <div className='body'>
      {
      	d.coupons && d.coupons.map((r, index) => {
          return <div className='d-flex mb-10'><div className='w-150px border-box pr-10'>
									<Select value={d.couponTemplateNumber} multiple={false} onChange={this.onCouponsItemChange.bind(this, "UPDATE", index, "couponTemplateNumber")} >
											{
												[].map(p => {
													return <Select.Option key={p.number} label={p.name} value={p.number} />
												})
											}
										</Select>
									</div><div className='w-150px border-box pr-10'>
									
									<Input append="" value={r.count} onChange={this.onCouponsItemChange.bind(this, "UPDATE", index, 'count')}></Input></div><div className='w-100px border-box'>
								<i className="color-red el-icon-circle-cross ml-10" onClick={this.onCouponsItemChange.bind(this, "DELETE", index)}></i>
							</div>
						</div>
          })
      	}
			</div>
		<Button type="primary" onClick={this.onCouponsItemChange.bind(this, "ADD")}>添加</Button>
	</React.Fragment>
</Form.Item>

{/* 
	onCouponsItemChange(type, index, key, value) {
		let { d } = this.props
		let { couponsList } = d
		switch(type) {
			case "ADD" : {
				couponsList.push({})
				break;
			}
			case "UPDATE": {
				couponsList[index][key] =value;
				break;
			}
			case "DELETE": {
				couponsList.splice(index, 1)
				break;
			}
		}
		this.props.actions.onStateNestChange("d", "couponsList",  couponsList)
	}
*/}

						
						
					
						
						
						
						
						
						
						
						
						
						
						
						
							
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
		filter={{ branchId: (detail && detail.branchIds) ? detail.branchIds.join(",") : "" }}
		onCancel={this.toggleBranchSelect.bind(this)}
		onConfirm={this.onBranchConfirm.bind(this)}
	></BranchSeletor>
}
						
					
					</React.Fragment>
				</FormPanelWapper>
				
<SeperateLine className='mb-20' />
				

		
			</Form>
		</div>
	</div>
}



