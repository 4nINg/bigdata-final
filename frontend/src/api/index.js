import axios from 'axios'

const apiUrl = '/api'

export default {
  signUp(params) {
    axios.post(`${apiUrl}/auth/signup/`, {
      params,
    })
  },  
  logIn(params) {
    return axios.post(`${apiUrl}/auth/login/`, {
      params,
    })
  },
  session(params){
    return axios.post(`${apiUrl}/auth/session/`, {
      params,
    })
  },
  async logOut(params){
    await axios.delete(`${apiUrl}/auth/logout/`, {
      data: {
        token : params,
      },
    })
  }

}