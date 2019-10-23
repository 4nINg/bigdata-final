<template>
  <div class="searchdetail_main">
    <product></product>
    <InfoandReview></InfoandReview>
  </div>
</template>
<script>
import product from "../Panel/Product";
import InfoandReview from "../Panel/InfoandReview";

export default {
  components: {
    product: product,
    InfoandReview: InfoandReview
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