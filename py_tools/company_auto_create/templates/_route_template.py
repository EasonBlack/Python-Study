from jinja2 import Template

route_template =  Template('''
GET           /api/{{routeName}}                                              controllers.{{entityName}}Controller.search{{entityName}}       
GET           /api/{{routeName}}/:id                                          controllers.{{entityName}}Controller.find{{entityName}}ById(id: Long)   
POST          /api/{{routeName}}                                              controllers.{{entityName}}Controller.save{{entityName}}       
PUT           /api/{{routeName}}                                              controllers.{{entityName}}Controller.update{{entityName}}   
''')