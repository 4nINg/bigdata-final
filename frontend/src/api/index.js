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
        return axios.post(`${apiUrl}/auth/login/`, {
            params,
        })
    },
    session(params) {
        return axios.post(`${apiUrl}/auth/session/`, {
            token: params,
        })
    },
    async logOut(params) {
        await axios.delete(`${apiUrl}/auth/logout/`, {
            data: {
                token: params,
            },
        })
    },
    async searchByKeyword(param) {
        return await axios.post(`${apiUrl}/serializer/product/`, {
            keyword: param
        })
    }
}