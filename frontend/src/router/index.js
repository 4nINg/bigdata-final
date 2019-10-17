import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from "../components/pages/MainPage"
import SearchPage from "../components/pages/SearchPage"
Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: MainPage, name: 'home' },
        { path: '/search', component: SearchPage, name: 'search' },

    ],
    scrollBehavior() {
        return { x: 0, y: 0 }
    },
})

export default router