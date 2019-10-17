<template>
  <div class="searchbox_main">
    <div class="searchbox_div">
      <div class="searchbox_input_div">
        <input class="searchbox_input" type="text" />
      </div>
      <div class="searchbox_icon">
        <span>
          <i class="fas fa-search" />
        </span>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.searchbox_main {
  width: 95%;
  margin-left: 2.5%;
  margin-right: 2.5%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.searchbox_div {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.searchbox_input_div {
  width: 100%;
  height: 5vh;
  background-color: rgba(40, 40, 40, 0.1);
  /* margin-left: 1%; */
  border-radius: 1vh;
  display: flex;
  justify-content: center;
}

.searchbox_icon {
  position: absolute;
  top: 50%;
  right: 3.5%;
  transform: translateX(-50%);
  transform: translateY(-50%);
  cursor: pointer;
}

.searchbox_input {
  width: 90%;
  height: 100%;
  outline: none;
}
</style>