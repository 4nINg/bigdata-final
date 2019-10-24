<template>
  <div class="award_main">
    <div class="award-top">
            <div>img</div>
    </div>
    <div class="award-container">
        <div class="award-header">
            <div>
                <span>2019&nbsp;</span><span>도담 어워드</span>
            </div>
        </div>
        <product
        v-for="(award, index) in awards"
        :key="index"
        :ranking="index"
        :imgurl="award.imgurl"
        :brand="award.brand"
        :productname="award.productname"
        :rating="award.rating"
        ></product>
        <div class="award-content">
            <div class="award-div">
                <div class="award_image">img</div>
                <div class="award_info">
                    <span>브랜드</span>
                </div>
            </div>
            <div class="award-div">
                <div class="award_image">img</div>
                <div class="award_info">
                    <span>브랜드</span>
                </div>
            </div>
            <div class="award-div">
                <div class="award_image">img</div>
                <div class="award_info">
                    <span>브랜드</span>
                </div>
            </div>
        </div>
    </div>


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
</style>
