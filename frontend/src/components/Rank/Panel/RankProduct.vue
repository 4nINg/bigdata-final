<template>
  <div class="rank_product">
    <div class="rank_product_img">
      <img :src="imgurl" />
    </div>
    <div class="rank_product_name">
      <span>{{productname}}</span>
    </div>
    <div class="rank_product_brand">
      <span>{{brand}}</span>
    </div>
  </div>
</template>
<script>
export default {
  props: ["imgurl", "productname", "brand"]
};
</script>
<style>
.rank_product {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 5%;
}

.rank_product_img {
  width: 100%;
  height: 60%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.rank_product_img img {
  height: 100%;
}

.rank_product_name,
.rank_product_brand {
  font-size: 0.7em;
  text-align: center;
  width: 80%;
  height: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>