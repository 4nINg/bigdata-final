<template>
  <div class="newproduct_main">
    <div class="newproduct_header">
      <span>new&nbsp;</span>
      <span>신규 등록 제품</span>
    </div>
    <div class="carousel_div">
      <carousel :nav="false" :items="1.3" :loop="true" :center="true" :dots="false" :margin="10">
        <div v-for="temp in temps" class="newProduct">
          <span>{{temp}}</span>
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
  data: () => ({
    temps: [
      "비타민1",
      "비타민2",
      "비타민3",
      "비타민4",
      "비타민5",
      "비타민6",
      "비타민7",
      "비타민8"
    ]
  })
};
</script>