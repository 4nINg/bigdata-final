import axios from 'axios'

const apiUrl = 'http://192.168.100.69:8000/api'
    // const apiUrl = '/api'

export default {
  signUp(params) {
    axios.post(`${apiUrl}/auth/signup/`, {
      params,
    })
  },  
  logIn(params) {
    return axios.post(`${apiUrl}/rest-auth/login/`, 
      params,
    )
  },
  session(params){
    return axios.get(`${apiUrl}/auth/userinfo/`, 
      params,
    )
  },
  async logOut(){
    await axios.post(`${apiUrl}/rest-auth/logout/`, 
  )},
  async searchByKeyword(param) {
    return await axios.post(`${apiUrl}/serializer/product/`, {
        keyword: param
    })
  },

}