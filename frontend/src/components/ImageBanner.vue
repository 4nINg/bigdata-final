<template>
  <div class="image_main">
    <div class="image_Banner">
      <div class="image_div"></div>
      <div class="image_div"></div>
      <div class="image_div"></div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.image_main {
  width: 100%;
  height: 157px;
  overflow: hidden;
}
.image_Banner {
  width: 300%;
  height: 100%;
}

.image_div {
  max-width: 736px;
  width: 100%;
  height: 300px;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: 50% 50%;
  float: left;
  animation: imageflow 6s infinite;
}

.image_div:nth-child(1) {
  background-image: url("../../image/joker.jpg");
}

.image_div:nth-child(2) {
  background-image: url("../../image/share.jpg");
}

.image_div:nth-child(3) {
  background-image: url("../../image/joker_my_page.jpg");
}

@keyframes imageflow {
  0% {
    transform: translateX(0);
  }
  33% {
    /* left: 736px; */
    transform: translateX(-100%);
  }
  66% {
    /* left: 1472px; */
    transform: translateX(-200%);
  }
  99% {
    transform: translateX(0);
  }
  100% {
    /* left: 0px; */
    transform: translateX(0);
  }
}
</style>