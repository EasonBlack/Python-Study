from jinja2 import Template

redux_action_template =  Template(''' 

import axios from 'axios'

export const search{{entityName}} = () => async dispatch => {
    let response =  await axios.get(`${ApiUrl}/api/{{routeName}}`)
    dispatch({type: "{{reduxName}}_FETCH",  list: response.data.data.data}) 
    return response;
}

export const find{{entityName}}ById = (id) => async dispatch => {
    let response =  await axios.get(`${ApiUrl}/api/{{routeName}}/${id}`)
    dispatch({type: "{{reduxName}}_FETCH_BY_ID",  value: response.data.data }) 
    return response;
}

export const find{{entityName}}New = ()  => {
    return {type: "{{reduxName}}_FETCH_NEW" }
}

export const save{{entityName}} = (obj) => async dispatch => {
    let response =  await axios.post(`${ApiUrl}/api/{{routeName}}`, obj)
    return response;
}
export const update{{entityName}} = (obj) => async dispatch => {
    let response =  await axios.put(`${ApiUrl}/api/{{routeName}}`, obj)
    return response;
}


import { search{{entityName}},  find{{entityName}}ById, save{{entityName}}, update{{entityName}} } from '../../../redux/actions/xxxxx'

var mapDispatchToProps = function (dispatch) {
  return {
    actions: bindActionCreators({
        onStateChange, onStateNestChange,
        search{{entityName}},  find{{entityName}}ById, save{{entityName}}, update{{entityName}}
    }, dispatch)
  };
}



''')