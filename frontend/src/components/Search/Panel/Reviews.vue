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
<style>
.reviews_main {
  width: 100%;
  max-height: 30vh;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
  margin-top: 1.5%;
  background-color: #fff;
  padding-bottom: 4%;
  border-bottom: 1px solid rgba(0, 0, 0, 0.4);
}

.reviews_user {
  width: 100%;
  height: 7vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.reviews_userinfo {
  width: 30%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.reviews_avatar {
  width: 40%;
  height: 80%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2em;
  border: 1px solid rgba(0, 0, 0, 0.4);
  border-radius: 50%;
}

.reviews_date {
  width: 30%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.reviews_container {
  width: 100%;
  max-height: 25vh;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
}

.reviews_rating {
  padding-left: 2%;
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.reviews_content {
  width: 100%;
  margin-left: 5%;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  margin-top: 4%;
  margin-bottom: 4%;
}

.reviews_heart {
  width: 100%;
  margin-left: 5%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  color: red;
}
</style>