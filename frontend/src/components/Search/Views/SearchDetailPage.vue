<template>
  <div class="searchdetail_main">
    <ProductProfile
      :imgurl="productDetail.imgurl"
      :productname="productDetail.productname"
      :brand="productDetail.brand"
    ></ProductProfile>
    <InfoandReview></InfoandReview>
  </div>
</template>
<script>
import ProductProfile from "../Panel/ProductProfile";
import InfoandReview from "../Panel/InfoandReview";
import { mapState } from "vuex";

export default {
  components: {
    ProductProfile: ProductProfile,
    InfoandReview: InfoandReview
  },
  computed: {
    ...mapState({
      productDetail: state => state.data.productDetail
    })
  }
};
</script>
<style>
.searchdetail_main {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>