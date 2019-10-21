<template>
  <div class="function_main">
    <div class="function">
      <span>Function1</span>
    </div>
    <div class="divider"></div>
    <div class="function">
      <span>Function2</span>
    </div>
    <div class="divider"></div>
    <div class="function">
      <span>Function3</span>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.function_main {
  width: 100%;
  height: 20vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 0.8vh;
  padding-bottom:1vh;
  background-color:#fff;
}

.function {
  width: 33%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.divider {
  width: 0.5%;
  height: 60%;
  background-color: rgba(0, 0, 0, 0.1);
}
</style>