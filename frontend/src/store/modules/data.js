import api from '../../api'

// initial state
const state = {
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
    }
}

// actions
const actions = {
    async searchMovies({ commit }, params) {
        const resp = await api.searchMovies(params)
        const movies = resp.data.map(d => ({
            id: d.id,
            title: d.title,
            genres: d.genres_array,
            viewCnt: d.view_cnt,
            rating: d.average_rating,
        }))

        commit('setMovieSearchList', movies)
    },
}

// mutations
const mutations = {
    setMovieSearchList(state, movies) {
        state.movieSearchList = movies.map(m => m)
    },
}

export default {
    namespaced: true,
    state,
    actions,
    mutations
}