<template>
  <div id="app">
    <!-- <v-app-bar app clipped-left color="indigo">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
      <span class="title ml-3 mr-5 white--text">영화 추천 서비스</span>
      <v-spacer />
    </v-app-bar>-->

    <!-- <v-navigation-drawer v-model="drawer" app clipped color="grey lighten-4">
      <v-list dense class="grey lighten-4">
        <template v-for="(choice, i) in choices">
          <v-list-item
            :key="i"
            @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ choice.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choice.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>-->

    <!-- each pages will be placed here -->
    <div class="main_div">
      <router-view />
    </div>
  </div>
</template>

<script>
import router from "./router";

export default {
  data: () => ({}),
  methods: {}
};
</script>

<style>
#app {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
}

.main_div {
  max-width: 736px;
  width: 100%;
  height: 100vh;
}
</style>