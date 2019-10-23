<template>
  <div class="header_main">
    <div class="logo_main" @click="goTo()">
      <img src="../../../image/logo/logo.svg" alt="DODAMDODMA" height="40" />
    </div>
    <div class="icon_main">
      <!-- <i class="far fa-bell logo_design"/> -->
      <v-icon class="logo_design" color="#fff">mdi-login-variant</v-icon>
      <v-icon class="logo_design" color="#fff" @click="logOut">mdi-logout-variant</v-icon>
      <i class="fas fa-user logo_design" />
    </div>
  </div>
</template>
<script>
import router from "../../router";
import { mapActions } from "vuex";

export default {
  methods: {
    goTo() {
      router.push("/");
    },
    ...mapActions("data", ["logOut"]),
  }
};
</script>
<style>
.header_main {
  background-color: #e85f63;
  width: 100%;
  height: 7.5vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo_main {
  width: 15%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-left: 2.5%;
  cursor: pointer;
  margin-top: -1%;
}

.icon_main {
  width: 18%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.logo_design {
  color: #fff;
  font-size: 1.4em;
}

.logo_design:last-child {
  margin-right: 10%;
}
</style>