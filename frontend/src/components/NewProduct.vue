<template>
  <div class="newproduct_main">
    <div class="newproduct_header">
      <span>신규 등록 제품</span>
    </div>
    <div class="newproduct_container">
      <div class="newproduct_content">
        <div class="product">
          <span></span>
          <span>비타민 1</span>
        </div>
        <div class="product">
          <span></span>
          <span>비타민 2</span>
        </div>
        <div class="product">
          <span></span>
          <span>비타민 3</span>
        </div>
        <div class="product">
          <span></span>
          <span>비타민 4</span>
        </div>
        <div class="product">
          <span></span>
          <span>비타민 5</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.newproduct_main {
  width: 100%;
  height: 20vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.newproduct_header {
  width: 100%;
  height: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.newproduct_container {
  width: 100%;
  height: 70%;
  /* display: flex;
  justify-content: center;
  align-items: center; */
  overflow: hidden;
}

.newproduct_content {
  width: 200%;
  height: 100%;
  float: left;
  display: flex;
  align-items: center;
}

.product {
  width: 30%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
  margin-right: 5%;
}
</style>