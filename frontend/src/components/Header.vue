<template>
  <div class="header_main">
    <div class="logo_main">
      <span>DODAM</span>
      <span>DODAM</span>
    </div>
    <div class="icon_main">
      <i class="far fa-bell" />
      <i class="fas fa-user" />
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.header_main {
  width: 100%;
  height: 8vh;
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
}

.icon_main {
  width: 15%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>