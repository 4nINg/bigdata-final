<template>
  <div class="userrank">
    <div class="rank_header">
      <span>유저 랭킹</span>
    </div>
    <div class="rank_menus">
      <div class="rank_menu">
        <span>
          <i class="far fa-bell" />
        </span>
      </div>
      <div class="rank_menu">
        <span>
          <i class="far fa-bell" />
        </span>
      </div>
      <div class="rank_menu">
        <span>
          <i class="far fa-bell" />
        </span>
      </div>
      <div class="rank_menu">
        <span>
          <i class="far fa-bell" />
        </span>
      </div>
      <div class="rank_menu">
        <span>
          <i class="far fa-bell" />
        </span>
      </div>
      <div class="rank_menu">
        <span>
          <i class="far fa-bell" />
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
  height: 20vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.rank_header {
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
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
  height: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.rank_menu {
  font-size: 2em;
}

.rank_menu:hover span {
  /* transform: scale(1.5); */
  border-bottom: 1px solid red;
}
</style>