<template>
  <div class="award_main">
    <NavigationBar/>
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
          v-for="(award, index) in sorted"
          :key="index"
          :ranking="index"
          :image_url="award.image_url"
          :company_name="award.company_name"
          :name="award.name"
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
import NavigationBar from "../../Base/NavigationBar";
import { mapState } from "vuex";

export default {
  components: {
    product: product,
    NavigationBar
  },
  computed: {
    ...mapState({
      awards: state => state.data.products
    }),
    sorted() {
      return this.awards.sort(function(a, b) {
        return b.rating - a.rating;
      });
    }
  }
};
</script>
<style>
</style>
