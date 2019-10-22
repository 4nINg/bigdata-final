<template>
  <div class="newproduct_main">
    <div class="newproduct_header">
      <span>new&nbsp;</span>
      <span>신규 등록 제품</span>
    </div>
    <div class="carousel_div">
      <carousel
        :nav="false"
        :items="1.3"
        :autoHeight="true"
        :loop="true"
        :center="true"
        :dots="false"
        :margin="10"
      >
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

<style>
.newproduct_main {
  width: 100%;
  height: 23vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: #fff;
  margin-top: 0.8vh;
  padding-bottom: 1vh;
}

.newproduct_header {
  width: 100%;
  height: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.newproduct_header span:first-child {
  color: #e85f63;
}

.carousel_div {
  width: 100%;
  height: 70%;
  position: relative;
  overflow: hidden;
}

.carousel_div div {
  height: 100%;
}

.newProduct {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border: 1px solid black;
}

/* .newproduct_container {
  width: 100%;
  height: 70%;
  overflow: hidden;
}
.newproduct_content {
  width: 200%;
  height: 100%;
  float: left;
  display: flex;
  align-items: center;
}
.product {
  width: 30%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
  margin-right: 1%;
  cursor: pointer;
} */

.swiper-container {
  width: 100%;
  height: 100%;
}
.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;
  /* Center slide text vertically */
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}
.swiper-pagination {
  position: absolute;
  top: 10px;
  right: 10px;
  width: auto !important;
  left: auto !important;
  margin: 0;
}
.swiper-pagination-bullet {
  padding: 5px 10px;
  border-radius: 0;
  width: auto;
  height: 30px;
  text-align: center;
  line-height: 30px;
  font-size: 12px;
  color: #000;
  opacity: 1;
  background: rgba(0, 0, 0, 0.2);
}
.swiper-pagination-bullet-active {
  color: #fff;
  background: #007aff;
}
</style>