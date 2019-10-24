<template>
  <div class="reviews_main">
    <div class="reviews_user">
      <div class="reviews_userinfo">
        <div class="reviews_avatar">
          <i class="far fa-user" />
        </div>
        <div class="reviews_nickname">
          <span>{{nickname}}</span>
        </div>
      </div>
      <div class="reviews_date">{{date}}</div>
    </div>
    <div class="reviews_container">
      <div class="reviews_rating">
        <v-rating
          v-model="review_rating"
          color="rgb(255,215,0)"
          background-color="rgb(255,215,0)"
          dense
        />
      </div>
      <div class="reviews_content">
        <p>너무 좋아요 만족 대만족</p>
      </div>
      <div class="reviews_heart">
        <i class="fas fa-heart" />
        <span>&nbsp;{{heartCnt}}</span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data: () => ({
    nickname: "나임",
    date: "2019.10.22",
    review_rating: 4,
    heartCnt: "5"
  })
};
</script>