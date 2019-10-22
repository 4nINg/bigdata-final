import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';
import store from './store';
import VueCarousel from "vue-owl-carousel";
import { mapActions } from 'vuex';

Vue.use(VueCarousel);


Vue.config.productionTip = false

new Vue({
    vuetify,
    router,
    store,
    render: h => h(App),
    created(){
      if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null){
        this.session(localStorage.getItem("token"))
      }
    },
    methods: {
      ...mapActions({
        session: 'data/session'
      })
    }
}).$mount('#app')