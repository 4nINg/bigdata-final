<template>
  <div class="navigation_bar">
    <div class="navigation_menu" @click="goTo(0)">
      <span>검색</span>
      <span class="line_span"></span>
    </div>
    <div class="navigation_menu margin_menu" @click="goTo(1)">
      <span>랭킹</span>
      <span class="line_span"></span>
    </div>
    <div class="navigation_menu margin_menu" @click="goTo(2)">
      <span>이벤트</span>
      <span class="line_span"></span>
    </div>
    <div class="navigation_menu" @click="goTo(3)">
      <span>어워드</span>
      <span class="line_span"></span>
    </div>
  </div>
</template>
<script>
import router from "../../router";
export default {
  data: () => ({}),
  methods: {
    goTo(n) {
      if (n == 0) {
        router.push("/search");
      } else if (n == 1) {
      } else if (n == 2) {
        router.push("/event");
      } else if (n == 3) {
      }
    }
  }
};
</script>
<style>
.navigation_bar {
  width: 100%;
  height: 7.5vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid lightgray;
  background-color:#fff;
  padding-left: 3%;
  padding-right: 3%;
}

.navigation_menu {
  /* width: 15%; */
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}


.navigation_menu:hover{
border-bottom: 3px solid #e85f63;
}
</style>