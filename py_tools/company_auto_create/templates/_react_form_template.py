
from jinja2 import Template

# from  ._react_form_input_template import *


react_form_template = Template('''
render() {
	let { detail } = this.props;
	let { currentTab } = this.state;

	return <div className='h-100 d-flex-column'>
		<TopNav title="{{formText}}" url="" />
		<DetailTop />
		<Menu defaultActive={currentTab} className="tab-nav" mode="horizontal" onSelect={this.onSelect.bind(this)}>
			<Menu.Item index="basic">基本信息</Menu.Item>
		</Menu>
		<div className='p-20 flex-1 overflow-y-auto'>
			<Form
				model={detail}
				ref="form" labelPosition="left" labelWidth="100"
				className= {'demo-ruleForm ' +  classNames({hide: currentTab != "basic"})} >
				
		
				{% for panal in panals %}
				<FormPanelWapper title="{{panal.name}}">
					<React.Fragment>
					{% for item in panal.items %}
						{% if item.type == "input" %}
							{{ form_input_template.render(title=item.title, props=item.props)  }}
						{% endif %}
						{% if item.type == "dateRange" %}
							{{ form_daterange_template.render(title=item.title, props=item.props)  }}
						{% endif %}
						{% if item.type == "color" %}
							{{ form_color_template.render(title=item.title, props=item.props)  }}
						{% endif %}
						{% if item.type == "image" %}
							{{ form_image_template.render(title=item.title, props=item.props)  }}
						{% endif %}
						{% if item.type == "switch" %}
							{{ form_switch_template.render(title=item.title, props=item.props)  }}
						{% endif %}
						{% if item.type == "textarea" %}
							{{ form_textarea_template.render(title=item.title, props=item.props)  }}
						{% endif %}
						{% if item.type == "radioBox" %}
							{{ form_radioBox_template.render(title=item.title, props=item.props, titles=item.title.split(","))  }}
						{% endif %}
						{% if item.type == "radioBoxGroup" %}
							{{ form_radioBoxGroup_template.render(title=item.title, props=item.props, titles=item.title.split(","))  }}
						{% endif %}
						{% if item.type == "checkBoxGroup" %}
							{{ form_checkBoxGroup_template.render(title=item.title, props=item.props)  }}
						{% endif %}
						{% if item.type == "customInput" %}
							{{ form_customInput_template.render(title=item.title, props=item.props, titles=item.title.split(","))  }}
						{% endif %}
						{% if item.type == "table" %}
							{{ form_table_template.render(title=item.title, props=item.props, titles=item.title.split(","))  }}
						{% endif %}
					{% endfor %}
					</React.Fragment>
				</FormPanelWapper>
				{{ form_seperate_template.render()  }}
				{% endfor %}

		
			</Form>
		</div>
	</div>
}




''')