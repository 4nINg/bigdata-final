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
