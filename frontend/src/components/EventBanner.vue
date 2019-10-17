<template>
  <div class="event_main">
    <div class="event_header">
      <span>이벤트</span>
    </div>
    <div class="event_container">
      <div class="event_content">
        <div class="event">
          <span></span>
          <span>이벤트 1</span>
        </div>
        <div class="event">
          <span></span>
          <span>이벤트 2</span>
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
  height: 25vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.event_header {
  width: 100%;
  height: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.event_container {
  width: 100%;
  height: 70%;
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
  border: 1px solid black;
  margin-right: 1%;
}
</style>