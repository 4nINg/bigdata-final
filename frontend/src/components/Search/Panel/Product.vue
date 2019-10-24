<template>
  <div class="searchdetail_product">
    <div class="searchdetail_header">
      <div class="searchdetail_backbtn" @click="back()">
        <span>
          <i class="fas fa-chevron-left" />
        </span>
      </div>
    </div>
    <div class="searchdetail_image">
      <img :src="imgurl" />
    </div>
    <div class="searchdetail_product_name">
      <div class="searchdetail_name">
        <span>{{productname}}</span>
      </div>
      <div class="searchdetail_brand">
        <span>{{brand}}</span>
      </div>
    </div>
  </div>
</template>
<script>
import router from "../../../router";
import { mapState } from "vuex";
export default {
  data: () => ({}),
  computed: {
    ...mapState({
      imgurl: state => state.data.productDetail.imgurl
    }),
    ...mapState({
      productname: state => state.data.productDetail.productname
    }),
    ...mapState({
      brand: state => state.data.productDetail.brand
    })
  },
  methods: {
    back() {
      router.go(-1);
    }
  }
};
</script>