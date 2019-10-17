<template>
  <div id="app">
    <div class="main_div">
      <Header />
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from "./components/Header";

export default {
  components: {
    Header: Header
  },
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
  align-items: center;
}

.main_div {
  max-width: 400px;
  max-height: 812px;
  width: 100%;
  height: 100vh;
}
</style>