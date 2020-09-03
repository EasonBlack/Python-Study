from jinja2 import Template

redux_template =  Template(''' 

import { basicReduxSwitch } from '../../util/helper'

export default function reducer(state = {
	rows: [],
  detail: {},
	totalPages: 0
}, action = {}) {
  let v = basicReduxSwitch(action, state);
  if (v) {
    return v
  }
  switch (action.type) {   
    case "{{reduxName}}_FETCH": {
			let list = action.list;
			return Object.assign({}, state, {
					rows: list.items || list,
					totalPages: list.totalPages || 0
			})
    }
    case "{{reduxName}}_FETCH_BY_ID": {
			let value = action.value;
			return Object.assign({}, state, {
					detail: value
			})
    }
    case "{{reduxName}}_FETCH_NEW": {
			let value = {};
			return Object.assign({}, state, {
					detail: value
			})
    }
    default: 
      return state
  }
}

''')