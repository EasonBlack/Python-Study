
import jinja2
import os

PATH = os.path.dirname(os.path.abspath(__file__))

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(PATH),
    variable_start_string='%%',
    variable_end_string='%%',
)

template = env.from_string('Hello %% name %%!')
templateFile = env.get_template('change-delimiter.html')
print(template.render(name='Eason'))
print(templateFile.render(name='Jason'))