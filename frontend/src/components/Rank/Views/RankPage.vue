<template>
  <div class="rankpage_main">
    <div class="rank_container">
      <div class="rank_header">
        <div>
          <span>남성&nbsp;</span>
          <span>랭킹</span>
        </div>
        <div class="rank_more_btn">
          <span>더보기</span>
        </div>
      </div>

      <div class="rank_content">
        <div class="product_div" v-for="product in manRank">
          <RankProduct
            :imgurl="product.imgurl"
            :productname="product.productname"
            :brand="product.brand"
          ></RankProduct>
        </div>
      </div>
    </div>
    <div class="rank_container">
      <div class="rank_header">
        <span>여성&nbsp;</span>
        <span>랭킹</span>
        <div class="rank_more_btn">
          <span>더보기</span>
        </div>
      </div>
      <div class="rank_content">
        <div class="product_div" v-for="product in manRank">
          <RankProduct
            :imgurl="product.imgurl"
            :productname="product.productname"
            :brand="product.brand"
          ></RankProduct>
        </div>
      </div>
    </div>
    <div class="rank_container age_container">
      <div class="rank_header">
        <span>연령별&nbsp;</span>
        <span>랭킹</span>
        <div class="rank_more_btn">
          <span>더보기</span>
        </div>
      </div>
      <div class="age_check_tab">
        <div class="age_check">아동·청소년</div>
        <div class="age_check">성인</div>
        <div class="age_check">장년</div>
      </div>
      <div class="rank_content age_content">
        <div class="product_div" v-for="product in manRank">
          <RankProduct
            :imgurl="product.imgurl"
            :productname="product.productname"
            :brand="product.brand"
          ></RankProduct>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import RankProduct from "../Panel/RankProduct";
export default {
  components: {
    RankProduct: RankProduct
  },
  data: () => ({
    manRank: [
      {
        imgurl:
          "http://img.danawa.com/prod_img/500000/060/122/img/3122060_1.jpg?shrink=500:500",
        productname: "얼라이브 원스데일리 멀티비타민",
        brand: "네이쳐스웨이"
      },
      {
        imgurl:
          "http://img.danawa.com/prod_img/500000/060/122/img/3122060_1.jpg?shrink=500:500",
        productname: "얼라이브 원스데일리 멀티비타민",
        brand: "네이쳐스웨이"
      },
      {
        imgurl:
          "http://img.danawa.com/prod_img/500000/060/122/img/3122060_1.jpg?shrink=500:500",
        productname: "얼라이브 원스데일리 멀티비타민",
        brand: "네이쳐스웨이"
      }
    ]
  })
};
</script>