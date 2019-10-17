<template>
  <div class="navigation_bar">
    <div class="navigation_menu" @click="goTo(0)">
      <span>검색</span>
    </div>
    <div class="navigation_menu" @click="goTo(1)">
      <span>랭킹</span>
    </div>
    <div class="navigation_menu" @click="goTo(2)">
      <span>이벤트</span>
    </div>
    <div class="navigation_menu" @click="goTo(3)">
      <span>어워드</span>
    </div>
  </div>
</template>
<script>
import router from "../router";
export default {
  data: {},
  methods: {
    goTo(n) {
      if (n == 0) {
        router.push("/search");
      } else if (n == 1) {
      } else if (n == 2) {
      } else if (n == 3) {
      }
    }
  }
};
</script>
<style>
.navigation_bar {
  width: 100%;
  height: 6vh;
  display: flex;
  justify-content: space-around;
  align-items: center;
  border-top: 1px solid red;
  border-bottom: 1px solid red;
}

.navigation_menu {
  width: 20%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
</style>