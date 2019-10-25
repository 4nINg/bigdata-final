<template>
  <div class="header_main">
    <div class="logo_main" @click="goTo()">
      <img src="../../../image/logo/logo_revised.svg" alt="DODAMDODMA" height="40" />
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