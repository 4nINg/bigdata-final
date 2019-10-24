<<<<<<< HEAD:frontend/src/components/Search/Panel/Product.vue
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
=======
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
export default {
  props: ["imgurl", "productname", "brand"],
  data: () => ({}),
  methods: {
    back() {
      router.go(-1);
    }
  }
};
</script>
<style>
.searchdetail_product {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.searchdetail_header {
  width: 100%;
  height: 6vh;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  background-color: #fff;
}

.searchdetail_backbtn {
  width: 10%;
  height: 10%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2em;
  cursor: pointer;
}

.searchdetail_image {
  width: 100%;
  max-height: 30vh;
  /* height: 100%; */
  min-height: 230px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  margin-bottom: 0.8vh;
}

.searchdetail_image img {
  width: 50%;
  height: 100%;
}

.searchdetail_product_name {
  width: 100%;
  height: 10vh;
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
  background-color: #fff;
  margin-bottom: 0.8vh;
}

.searchdetail_brand {
  padding: 0.5vh;
  border: 1px solid rgba(0, 0, 0, 0.4);
  margin-bottom: 1vh;
}
</style>
>>>>>>> 81cf195932fe0edb306c505a4160a95a2d7643bf:frontend/src/components/Search/Panel/ProductProfile.vue
