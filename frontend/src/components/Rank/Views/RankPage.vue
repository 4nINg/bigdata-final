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
<style>
.rankpage_main {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.rank_container {
  width: 100%;
  height: 25vh;
  display: flex;
  flex-direction: column;
  padding-top: 1%;
  background-color: #fff;
  margin-bottom: 1%;
}

.rank_header {
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.rank_header span:first-child {
  color: #e85f63;
}

.rank_more_btn {
  position: absolute;
  right: 5%;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 0.7em;
}

.age_check_tab {
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  box-shadow: 0px 1px 0px 0px rgba(0, 0, 0, 0.2);
}

.age_check {
  width: 30%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1%;
}

.age_check:hover {
  background-color: red;
}

.rank_content {
  width: 100%;
  height: 80%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.product_div {
  width: 30%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.prodcut_img {
  width: 70%;
  height: 50%;
}

.product_info {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.age_container {
  height: 30vh;
}
</style>