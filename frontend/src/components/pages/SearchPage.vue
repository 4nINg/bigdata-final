<template>
  <div class="searchpage_main">
    <div class="searchpage_input">
      <input type="text" />
      <i class="fas fa-search" />
    </div>
    <div class="current_keyword">
      <div class="current_keyword_header">
        <span>최근 검색어</span>
      </div>
      <div></div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.searchpage_main {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.searchpage_input {
  width: 95%;
  height: 5vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.searchpage_input input[type="text"] {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.2);
  outline: none;
  border-radius: 8px;
}

.searchpage_input i {
  position: absolute;
  left: 2%;
  top: 50%;
  transform: translateY(-50%);
}

.current_keyword {
  width: 100%;
  height: 91vh;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
}

.current_keyword_header {
  width: 95%;
  height: 6%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  border-top: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  margin-top: 2%;
}

.backBtn {
  width: 15%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
</style>