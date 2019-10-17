<template>
  <div class="Interest_main">
    <div class="Interest_container">
      <div class="Interest_header">
        <span class="header_content">관심 부분별 제품 찾기</span>
        <span class="line_span"></span>
      </div>
      <div class="Interest_list">
        <div class="icons">
          <div class="icon">
            <i class="fas fa-bars" />
            <span>1</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>2</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>3</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>4</span>
          </div>
        </div>
        <div class="icons">
          <div class="icon">
            <i class="fas fa-bars" />
            <span>5</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>6</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>7</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>8</span>
          </div>
        </div>
        <div class="icons">
          <div class="icon">
            <i class="fas fa-bars" />
            <span>9</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>10</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>11</span>
          </div>
          <div class="icon">
            <i class="fas fa-bars" />
            <span>12</span>
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
.Interest_main {
  width: 100%;
  height: 40vh;
}

.Interest_container {
  width: 95%;
  height: 100%;
  margin-left: 2.5%;
  margin-right: 2.5%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.Interest_header {
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
  /* margin-bottom: 0.5%; */
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

.Interest_list {
  width: 100%;
  height: 85%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.icons {
  width: 100%;
  height: 33%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.icon {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 20px;
}
</style>