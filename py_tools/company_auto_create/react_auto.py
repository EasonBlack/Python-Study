# coding=utf-8
import re
import sys, getopt
import argparse
from jinja2 import Template

from templates._react_form_template import *
from templates.form_components._react_form_input_template import *
from templates.form_components._react_form_daterange_template import *
from templates.form_components._react_form_color_template import *
from templates.form_components._react_form_image_template import *
from templates.form_components._react_form_switch_template import *
from templates.form_components._react_form_textarea_template import *
from templates.form_components._react_form_radioBox_template import *
from templates.form_components._react_form_radioBoxGroup_template import *
from templates.form_components._react_form_customInput_template import *
from templates.form_components._react_form_seperate_template import *
from templates.form_components._react_form_checkBoxGroup_template import *
from templates.form_components._react_form_table_template import *

formMainParse = argparse.ArgumentParser()
formMainParse.add_argument("-formTitle")
formMainParse.add_argument("-tabTitle")

formPanelParse = argparse.ArgumentParser()
formPanelParse.add_argument("--panel")
formPanelParse.add_argument("--item", nargs=argparse.REMAINDER)
# formMainArg = parser.parse_args(["-v", "12", "-b", "aaaaa", "-tableName", "BBBBB"])

class FormPanel:
	pass

class FormPanelItem:
	pass


fi = open("_form.txt", 'r+', encoding='utf8')
r = fi.readlines()
panals = []
currentPanel = None
for index,l in enumerate(r):
	if index==0:
		_temp = l.split(" ")
		formMainArg = formMainParse.parse_args(l.split(" "))
	else: 
		_temp = l.split(" ")
		formPanelArg = formPanelParse.parse_args(l.split("\t"))
		if formPanelArg.panel: 
			print(formPanelArg.panel.replace("\n", ""))
			if currentPanel:
				print(12)
				panals.append(currentPanel)
			currentPanel = FormPanel()
			currentPanel.name =formPanelArg.panel.replace("\n", "")
			currentPanel.items = []
		if formPanelArg.item:
			_key = formPanelArg.item[0]
			print(formPanelArg.item)
			#  _type = formPanelArg.item[1].replace("\n", "")
			_currentPanelItem = FormPanelItem()
			_currentPanelItem.props = formPanelArg.item[0].split(",")
			_currentPanelItem.type = formPanelArg.item[1]
			_currentPanelItem.title = formPanelArg.item[2].replace("\n", "")
			currentPanel.items.append(_currentPanelItem)

if currentPanel:
	panals.append(currentPanel)

print(panals)
print(panals[0].name)
print(panals[0].items[0].type)


# for index,l in enumerate(r):
# 	if l.startwith('\t')

	

print(formMainArg.formTitle)
print(formMainArg.tabTitle)

reactFromTamplateResult = react_form_template.render(
	formTitle=formMainArg.formTitle,
	tabTitle=formMainArg.tabTitle,  
	Template=Template,
	form_input_template=form_input_template, 
	form_daterange_template=form_daterange_template,
	form_color_template=form_color_template,
	form_image_template=form_image_template,
	form_switch_template=form_switch_template,
	form_textarea_template= form_textarea_template,
	form_radioBox_template = form_radioBox_template,
	form_radioBoxGroup_template = form_radioBoxGroup_template,
	form_customInput_template = form_customInput_template,
	form_seperate_template = form_seperate_template,
	form_checkBoxGroup_template = form_checkBoxGroup_template,
	form_table_template = form_table_template,
	panals = panals
)

f =  open("dict/test.js",'w', encoding='utf8')
f.write(reactFromTamplateResult)
f.close()



