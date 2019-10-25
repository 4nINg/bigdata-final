<template>
  <div class="ingredient_main">
    <div class="ingredient_container">
      <div class="ingredient_header">
        <span class="header_content">성분 종류 제품 찾기</span>
        <span class="line_span"></span>
      </div>
      <div class="ingredient_list">
        <div class="ingredients">
          <div class="ingredient rightLine">
            <span>1번</span>
            <i class="fas fa-chevron-right" />
          </div>
          <div class="ingredient">
            <span>2번</span>
            <i class="fas fa-chevron-right" />
          </div>
        </div>
        <div class="ingredients">
          <div class="ingredient rightLine">
            <span>3번</span>
            <i class="fas fa-chevron-right" />
          </div>
          <div class="ingredient">
            <span>4번</span>
            <i class="fas fa-chevron-right" />
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
.ingredient_main {
  width: 100%;
  height: 30vh;
}

.ingredient_container {
  width: 95%;
  height: 100%;
  margin-left: 2.5%;
  margin-right: 2.5%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.ingredient_header {
  width: 100%;
  height: 15%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.header_content {
  width: 100%;
  height: 99%;
  display: flex;
  align-items: center;
}

.line_span {
  content: "";
  width: 100%;
  height: 10%;
  margin-top: 0.5%;
  background-color: rgba(0, 0, 0, 0.1);
}

.ingredient_list {
  width: 100%;
  height: 85%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.ingredients {
  width: 100%;
  height: 48%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

.ingredient {
  width: 48%;
  height: 50%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}

.rightLine {
  border-right: 1px solid rgba(0, 0, 0, 0.1);
}

.ingredient .fas {
  margin-right: 10%;
}
</style>