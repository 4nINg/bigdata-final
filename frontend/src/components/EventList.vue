<template>
  <div class="eventlist_main">
    <div class="eventlist_event">
      <span>이벤트1</span>
    </div>
    <div class="eventlist_event">
      <span>이벤트2</span>
    </div>
    <div class="eventlist_event">
      <span>이벤트3</span>
    </div>
    <div class="eventlist_event">
      <span>이벤트4</span>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.eventlist_main {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.eventlist_event {
  width: 100%;
  height: 25vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1%;
  border: 1px solid black;
}
</style>