<template>
  <div class="award_main">
    <div class="award_banner"></div>
    <product
      v-for="(award, index) in awards"
      :key="index"
      :ranking="index"
      :imgurl="award.imgurl"
      :brand="award.brand"
      :productname="award.productname"
      :rating="award.rating"
    ></product>
  </div>
</template>
<script>
import product from "../../Base/Product";
import { mapState } from "vuex";

export default {
  components: {
    product: product
  },
  computed: {
    ...mapState({
      awards: state => state.data.products
    })
  }
};
</script>
<style>
.award_main {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.award_banner {
  width: 100%;
  height: 15vh;
  background-image: url("../../../../image/banner/event/three.png");
  background-size: cover;
  background-position: center center;
}
</style>
