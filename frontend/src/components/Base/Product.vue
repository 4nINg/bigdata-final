<template>
  <div class="product_forlist_main">
    <div class="rankDiv" v-if="ranking != -1">{{ranking+1}}</div>
    <div class="product_forlist_imgdiv">
      <img :src="image_url" />
    </div>
    <div class="product_forlist_productinfo">
      <div class="product_forlist_brand">{{company_name}}</div>
      <div class="product_forlist_productname">{{name}}</div>
      <div class="product_forlist_rating" v-if="ranking != -1">
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
  props: {
    ranking: {
      type: Number,
      default: -1
    },
    image_url: {
      type: String,
      default: ""
    },
    company_name: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: -1
    },
    name: {
      type: String,
      default: ""
    }
  }
};
</script>
