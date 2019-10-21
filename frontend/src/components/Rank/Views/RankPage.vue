<template>
  <div class="rankpage_main">
    <div class="rank_container">
      <div class="rank_header">
        <div>
        <span>남성&nbsp;</span><span>랭킹</span>
        </div>
        <div class="rank_more_btn">
            <span>더보기</span>
        </div>
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
        <span>여성&nbsp;</span><span>랭킹</span>
        <div class="rank_more_btn">
            <span>더보기</span>
        </div>
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
        <span>연령별&nbsp;</span><span>랭킹</span>
        <div class="rank_more_btn">
            <span>더보기</span>
        </div>
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
  height: 25vh;
  display: flex;
  flex-direction: column;
  padding-top: 1%;
  border-top: 1px solid black;
}

.rank_header {
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}


.rank_header span:first-child
{
    color:#e85f63;
}

.rank_more_btn{
    position: absolute;
    right: 5%;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    font-size:0.7em;
}

.rank_content {
  width: 100%;
  height: 100%;
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
</style>