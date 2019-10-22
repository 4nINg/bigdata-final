<template>
  <div class="event_main">
    <div class="event_header">
      <span>이벤트</span>
    </div>
    <div class="carousel_div">
      <carousel
        :nav="false"
        :items="2"
        :autoHeight="true"
        :loop="true"
        :center="true"
        :autoplaySpeed="true"
        :dots="false"
        :autoplayHoverPause="true"
        :margin="10"
      >
        <div v-for="banner in bannerlist" class="event">
          <img :src="banner.src" />
        </div>
      </carousel>
    </div>
    <!-- <div class="event_container">
      <div class="event_content">
        <div v-for="banner in bannerlist" class="event">
          <img v-bind:src="banner.src">
        </div>
      </div>
    </div>-->
  </div>
</template>
<script>
import carousel from "vue-owl-carousel";
export default {
  data: function() {
    return {
      bannerlist: [
        {
          src:
            "https://i0.wp.com/wp.americandatabank.com/wp-content/uploads/2016/03/banner-drug-testing.jpg"
        },
        {
          src:
            "https://i0.wp.com/wp.americandatabank.com/wp-content/uploads/2016/03/banner-drug-testing.jpg"
        },
        {
          src:
            "https://i0.wp.com/wp.americandatabank.com/wp-content/uploads/2016/03/banner-drug-testing.jpg"
        },
        {
          src:
            "https://i0.wp.com/wp.americandatabank.com/wp-content/uploads/2016/03/banner-drug-testing.jpg"
        }
      ]
    };
  },
  components: {
    carousel
  }
};
</script>
<style>
.event_main {
  width: 100%;
  height: 24vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: #fff;
  margin-top: 0.8vh;
  padding-bottom: 1vh;
}

.event_header {
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* .event_container {
  width: 100%;
  height: 80%;
  overflow: hidden;
}

.event_content {
  width: 400%;
  height: 100%;
  float: left;
  display: flex;
  align-items: center;
}

.event {
  width: 80%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 1%;
}

.event img{
  width: 100%;

} */

.carousel_div img {
  width: 100%;
}
</style>