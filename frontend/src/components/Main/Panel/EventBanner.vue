<template>
  <div class="event_main">
    <div class="event_header">
      <span>이벤트</span>
    </div>
    <div class="carousel_div">
      <carousel :nav="false" :items="1.2" :loop="true" :center="true" :dots="false" :margin="10">
        <div v-for="banner in bannerlist" class="event">
          <img :src="banner.src" />
        </div>
      </carousel>
    </div>
  </div>
</template>
<script>
import carousel from "vue-owl-carousel";
export default {
  components: {
    carousel
  },
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
  }
};
</script>