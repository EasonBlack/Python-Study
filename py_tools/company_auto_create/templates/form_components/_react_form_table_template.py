from jinja2 import Template

form_table_template =  Template('''

<Form.Item label=""  className='no-ml-form' >
   <React.Fragment>
			<div className=' d-flex'>
				{%- for title in titles %}
					{%- if loop.index0 % 3 == 0 -%}
						<div className='w-150px'>{{title}}</div>
					{%- endif -%}
				{%- endfor %}
				<div className='w-100px'></div>
			</div>
      <div className='body'>
      {
      	d.{{props[0]}} && d.{{props[0]}}.map((r, index) => {
          return <div className='d-flex mb-10'>
						{%- for title in titles %}
							{%- if loop.index0 % 3 == 0 -%}
								<div className='w-150px border-box pr-10'>
									{% if titles[loop.index0 + 1] == "select" -%}
										<Select value={d.{{titles[loop.index0+2]}}} multiple={false} onChange={this.on{{capitalizeProp}}ItemChange.bind(this, "UPDATE", index, "{{titles[loop.index0+2]}}")} >
											{
												[].map(p => {
													return <Select.Option key={p.number} label={p.name} value={p.number} />
												})
											}
										</Select>
									{%- endif %}
									{% if titles[loop.index0 + 1] == "input" -%}
										<Input append="" value={r.{{titles[loop.index0+2]}}} onChange={this.on{{capitalizeProp}}ItemChange.bind(this, "UPDATE", index, '{{titles[loop.index0+2]}}')}></Input>
									{%- endif -%}
								</div>
							{%- endif -%}
						{%- endfor -%}
							
							<div className='w-100px border-box'>
								<i className="color-red el-icon-circle-cross ml-10" onClick={this.on{{capitalizeProp}}ItemChange.bind(this, "DELETE", index)}></i>
							</div>
						</div>
          })
      	}
			</div>
		<Button type="primary" onClick={this.on{{capitalizeProp}}ItemChange.bind(this, "ADD")}>添加</Button>
	</React.Fragment>
</Form.Item>

{/* 
	on{{capitalizeProp}}ItemChange(type, index, key, value) {
		let { d } = this.props
		let { {{props[0]}}List } = d
		switch(type) {
			case "ADD" : {
				{{props[0]}}List.push({})
				break;
			}
			case "UPDATE": {
				{{props[0]}}List[index][key] =value;
				break;
			}
			case "DELETE": {
				{{props[0]}}List.splice(index, 1)
				break;
			}
		}
		this.props.actions.onStateNestChange("d", "{{props[0]}}List",  {{props[0]}}List)
	}
*/}

''')