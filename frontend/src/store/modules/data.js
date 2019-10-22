import api from '../../api'

// initial state
const state = {
  userInfo: null,
}

// actions
const actions = {
  async signUp({commit}, params){
    await api.signUp(params)
  },
  async logIn({commit}, params){
    var resp = await api.logIn(params).then((loginInfo)=>{
      return loginInfo.data
    });
    if (resp.is_authenticated){
      var userInfo = {
        email: resp.email,
        token: resp.token,
        nickname: resp.nickname
      }
      commit('setUserInfo', userInfo) 
      localStorage.setItem("token", state.userInfo.token) //로컬에 저장
      return true
    } else {
      return false
    }
  },
  async sessionStorage({commit}, params){
    return await api.session(params).then((loginInfo)=>{
      if (loginInfo.data.is_authenticated){
        var userInfo = {
          email: resp.email,
          token: resp.token,
          nickname: resp.nickname
        }
        commit('setUserInfo', userInfo)
      } else {
        localStorage.removeItem('token');
        commit('setUserInfo', null);
      }
    })
  },
}
// mutations
const mutations = {
  setUserInfo(state, userInfo) {
    state.userInfo = userInfo
  },
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}