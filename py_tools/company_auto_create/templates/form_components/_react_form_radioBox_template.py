from jinja2 import Template

form_radioBox_template =  Template('''
<Form.Item>
	<Radio.Group value={d.{{props[0]}}} onChange={this.onBasicChange.bind(this, '{{props[0]}}')}>
		{% for title in titles %}
			<Radio className = {'radio_item_wrapper  ' +  classNames({active: d.{{props[0]}} == '{{loop.index0}}'  })}
				value={ '{{loop.index0}}' } 
				checked={d.{{props[0]}} == '{{loop.index0}}' }>{{title}}
			</Radio>
		{% endfor %}
	</Radio.Group>
</Form.Item>
''')