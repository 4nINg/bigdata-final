<template>
  <div id="app">
    <div class="main_div">
      <Header />
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from "./components/Base/Header";

export default {
  components: {
    Header: Header
  },
  data: () => ({}),
  methods: {}
};
</script>
