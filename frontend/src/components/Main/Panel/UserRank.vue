<template>
  <div class="userrank">
    <div class="rank_header">
      <span>유저&nbsp;</span><span>랭킹</span>
    </div>
    <div class="rank_menus">
      <div class="rank_menu">
        <img src="../../../../image/icons/rank/man.png"/>
        <span>
          남성
        </span>
      </div>
      <div class="rank_menu">
        <img src="../../../../image/icons/rank/woman.png"/>
        <span>
          여성
        </span>
      </div>
      <div class="rank_menu">
        <img src="../../../../image/icons/rank/function.png"/>
        <span>
          기능별
        </span>
      </div>
      <div class="rank_menu">
       <img src="../../../../image/icons/rank/age.png"/>
        <span>
          연령대
        </span>
      </div>
      <div class="rank_menu">
        <img src="../../../../image/icons/rank/company.png"/>
        <span>
          브랜드
        </span>
      </div>
      <div class="rank_menu">
        <img src="../../../../image/icons/rank/nutrition.png"/>
        <span>
          영양소
        </span>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.userrank {
  width: 100%;
  height: 30vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color:#fff;
  margin-top:0.6vh;
}

.rank_header {
  width: 100%;
  height: 15%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size:1em;
  font-weight: 800;
}
.rank_header span:chil {
  color:#e85f63;
}

.rank_menus {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  flex: auto;
  justify-content: space-around;
  align-items: center;
}

.rank_menu {
  width: 30%;
  height: 45%;
  border-radius:15%;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  
}

.rank_menu img{
  width: 35px;
  cursor: pointer;
}

.rank_menu span{
  cursor: pointer;
}

.rank_menu span{
  font-size:0.4em;
}



.rank_menu {
  font-size: 2em;
}

</style>