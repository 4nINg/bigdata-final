import api from '../../api'

// initial state
const state = {
    userInfo: null,
    // shape: [{ id, title, genres, viewCnt, rating }]
    movieSearchList: [],
    productDetail: {
      imgurl: "http://img.danawa.com/prod_img/500000/060/122/img/3122060_1.jpg?shrink=500:500",
      productname: "얼라이브 원스데일리 멀티비타민",
      brand: "네이쳐스웨이",
      funcs: ["눈건강", "에너지 생성", "세포 재생", "숙취해소", "면역력 증진"],
      dailyintake: "1일 1회 1캡슐",
      reviewCnt: 5,
      rating: 4
    },
    products: [{
      imgurl: "https://d9vmi5fxk1gsw.cloudfront.net/home/glowmee/upload/20170105/1483607958793.png",
      brand: "바세린 (Vaseline)",
      productname: "퓨어 스킨 젤리 오리지날",
      rating: 5
    }, {
      imgurl: "https://www.koreadepart.com/data/item/1429064957_l1",
      brand: "유리아쥬 (URIAGE)",
      productname: "스틱레브르 오리지널",
      rating: 4
    }],
    manRank: [],
    womanRank: [],
    ageRank: []
}

// actions
const actions = {
  async signUp({ commit }, params) {
    await api.signUp(params)
  },
  async logIn({ commit }, params) {
    var resp = await api.logIn(params).then((loginInfo) => {
        return loginInfo.data
    });
    if (resp.is_authenticated) {
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
  async session({ commit }, params) {
    var resp = await api.session(params).then((loginInfo) => {
      if (loginInfo.data.is_authenticated) {
          var userInfo = {
            email: loginInfo.data.email,
            token: loginInfo.data.token,
            nickname: loginInfo.data.nickname
          }
          commit('setUserInfo', userInfo)
      } else {
          localStorage.removeItem('token');
          commit('setUserInfo', null);
      }
    })
  },
  async logOut({ commit }) {
    return await api.logOut(localStorage.getItem('token')).then(() => {
      localStorage.removeItem('token');
      commit('setUserInfo', null);
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