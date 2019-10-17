<template>
  <div class="navigation_bar">
    <div>
      <div class="menu_div">
        <i class="fas fa-bars" />
        <span class="menu_text">1번메뉴</span>
      </div>
    </div>
    <div>
      <div class="menu_div">
        <i class="fas fa-bars" />
        <span class="menu_text">2번메뉴</span>
      </div>
    </div>
    <div>
      <div class="menu_div">
        <i class="fas fa-bars" />
        <span class="menu_text">3번메뉴</span>
      </div>
    </div>
    <div>
      <div class="menu_div">
        <i class="fas fa-bars" />
        <span class="menu_text">4번메뉴</span>
      </div>
    </div>
    <div>
      <div class="menu_div">
        <i class="fas fa-bars" />
        <span class="menu_text">5번메뉴</span>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.navigation_bar {
  max-width: 736px;
  width: 100%;
  height: 8%;
  box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 1.4em;
  text-align: center;
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  background-color: white;
}

.navigation_bar > div {
  cursor: pointer;
}

.menu_div {
  display: flex;
  flex-direction: column;
}

.menu_text {
  font-size: 0.6em;
}
</style>