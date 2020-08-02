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

export const save{{entityName}} = (obj) => async dispatch => {
    let response =  await axios.post(`${ApiUrl}/api/{{routeName}}`, obj)
    return response;
}
export const update{{entityName}} = (obj) => async dispatch => {
    let response =  await axios.put(`${ApiUrl}/api/{{routeName}}`, obj)
    return response;
}



''')