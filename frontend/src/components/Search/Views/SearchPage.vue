<template>
  <div class="searchpage_main">
    <div class="searchpage_input">
      <input type="text" placeholder="제품명, 성분명, 브랜드명을 검색하세요."/>
      <i class="fas fa-search" aria-hidden="true"/>
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
  background-color:#fff;
}

.searchpage_input {
  width: 95%;
  height: 5vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  
}

.searchpage_input i {
  position: absolute;
  left: 0;
  padding: 9px 8px;
  top: 50%;
  color:#aaa;
  transform: translateY(-50%);
}

.searchpage_input input[type="text"] {
  width: 100%;
  height: 100%;
  outline: none;
  background-color:rgba(224, 222, 222, 0.2);
  border-radius:4px;
  padding-left:30px;
}

.searchpage_input input[type="text"]:focus{
  border-color:#e85f63;
  box-shadow: 0 0 5px 0 #e85f63;
}


.searchpage_input input[type="text"]:focus + i {
  color:#e85f63;
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
  width: 100%;
  height: 6%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  border-top: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  margin-top: 2%;
  
}
.current_keyword_header span{
margin-left:3%;
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