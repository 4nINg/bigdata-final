<template>
  <div class="searchdetail_container">
    <div class="searchdetail_dividediv">
      <div class="searchdetail_info div_active" @click="show_func()">
        <span>정보분석</span>
      </div>
      <div class="searchdetail_review" @click="show_review()">
        <span>
          사용자리뷰
          <span>
            (
            <span>{{reviewCnt}}</span>
            )
          </span>
        </span>
      </div>
    </div>
    <div v-if="show_function" class="searchdetail_container">
      <div class="searchdetail_content">
        <div class="searchdetail_function">
          <div v-for="func in funcs" class="product_function">
            <i class="fas fa-brain" />
            <span>{{func}}</span>
          </div>
        </div>
        <div class="searchdetail_intake_quantity">
          <div class="intake_header">
            <span>일일섭취량</span>
          </div>
          <div>
            <span>{{dailyintake}}</span>
          </div>
        </div>
      </div>
    </div>
    <div v-if="!show_function" class="review_container">
      <div class="review_header">
        <div>
          <span>제품 리뷰</span>
        </div>
      </div>
      <div class="rating_div">
        <div class="rating">
          <v-rating
            v-model="rating"
            color="rgb(255,215,0)"
            background-color="rgb(255,215,0)"
            dense
          />
        </div>
        <div class="rating">
          <span>{{rating}}</span>
          <span class="color_active">&nbsp;/ 5</span>
        </div>
      </div>
      <Reviews></Reviews>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import Reviews from "./Reviews";

export default {
  components: {
    Reviews: Reviews
  },
  data: () => ({
    show_function: true
  }),
  computed: {
    ...mapState({
      reviewCnt: state => state.data.productDetail.reviewCnt
    }),
    ...mapState({
      funcs: state => state.data.productDetail.funcs
    }),
    ...mapState({
      dailyintake: state => state.data.productDetail.dailyintake
    }),
    ...mapState({
      rating: state => state.data.productDetail.rating
    })
  },
  methods: {
    show_review() {
      var searchdetail_review = document.querySelector(".searchdetail_review");
      if (searchdetail_review.className.includes("div_active")) {
        return false;
      } else {
        document.querySelector(".div_active").classList.remove("div_active");
        searchdetail_review.classList.add("div_active");
        this.show_function = !this.show_function;
      }
    },
    show_func() {
      var searchdetail_info = document.querySelector(".searchdetail_info");
      if (searchdetail_info.className.includes("div_active")) {
        return false;
      } else {
        document.querySelector(".div_active").classList.remove("div_active");
        searchdetail_info.classList.add("div_active");
        this.show_function = !this.show_function;
      }
    }
  }
};
</script>