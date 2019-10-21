<template>
  <div class="rankpage_main">
    <div class="rank_container">
      <div class="rank_header">
        <span>남성 랭킹</span>
      </div>
      <div class="rank_content">
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
      </div>
    </div>
    <div class="rank_container">
      <div class="rank_header">
        <span>여성 랭킹</span>
      </div>
      <div class="rank_content">
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
      </div>
    </div>
    <div class="rank_container">
      <div class="rank_header">
        <span>연령별 랭킹</span>
      </div>
      <div class="rank_content">
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
        <div class="product_div">
          <div class="prodcut_img">img</div>
          <div class="product_info">
            <span>제품 이름</span>
            <span>제조사</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.rankpage_main {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.rank_container {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.rank_header {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.rank_content {
  width: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.product_div {
  width: 30%;
  display: flex;
  flex-direction: column;
}

.prodcut_img {
  width: 80%;
  height: 80%;
}

.product_info {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>