<template>
  <div class="event_main">
    <div class="event_header">
      <span>이벤트</span>
    </div>
    <div class="event_container">
      <div class="event_content">
        <div class="event">
          <img src="../../../../image/banner/event/three.png">
        </div>
        <div class="event">
         <img src="../../../../image/banner/event/three.png">
        </div>
        <div class="event">
          <span></span>
          <span>이벤트 3</span>
        </div>
        <div class="event">
          <span></span>
          <span>이벤트 4</span>
        </div>
        <div class="event">
          <span></span>
          <span>이벤트 5</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.event_main {
  width: 100%;
  height: 24vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color:#fff;
  margin-top:0.8vh;
  padding-bottom:1vh;
}

.event_header {
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.event_container {
  width: 100%;
  height: 80%;
  overflow: hidden;
}

.event_content {
  width: 400%;
  height: 100%;
  float: left;
  display: flex;
  align-items: center;
}

.event {
  width: 80%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  /* border: 1px solid black; */
  margin-right: 1%;
}

.event img{
  width: 100%;

}
</style>