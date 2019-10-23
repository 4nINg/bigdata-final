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