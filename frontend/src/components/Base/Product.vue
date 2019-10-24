<template>
  <div class="product_forlist_main">
    <div class="rankDiv">{{ranking+1}}</div>
    <div class="product_forlist_imgdiv">
      <img :src="imgurl" />
    </div>
    <div class="product_forlist_productinfo">
      <div class="product_forlist_brand">{{brand}}</div>
      <div class="product_forlist_productname">{{productname}}</div>
      <div class="product_forlist_rating">
        <v-rating v-model="rating" color="rgb(255,215,0)" background-color="rgb(255,215,0)" dense />
        <div class="ratingnumberdiv">
          <span>{{rating}}</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ["ranking", "imgurl", "brand", "productname", "rating"]
};
</script>
<style>
.product_forlist_main {
  width: 100%;
  height: 15vh;
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 0.1%;
  background-color: #fff;
}

.rankDiv {
  width: 7%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.product_forlist_imgdiv {
  width: 30%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.product_forlist_imgdiv img {
  max-width: 110px;
  max-height: 100px;
}

.product_forlist_productinfo {
  width: 50%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-direction: column;
}

.product_forlist_brand,
.product_forlist_productname,
.product_forlist_rating {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.product_forlist_brand {
  color: rgba(0, 0, 0, 0.5);
}

.ratingnumberdiv {
  width: 10%;
  text-align: center;
}
</style>