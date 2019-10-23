<template>
  <div id="eventpage" class="eventlist_main">
    <div v-for="item in event" class="eventlist_event">
      <span>{{item.text}}</span>
    </div>
  </div>
</template>

<script>
export default{
  data:function() {
    return{
      event:[
              { text: '이벤트1'},
              { text: '이벤트2'},
              { text: '이벤트3'},
              { text: '이벤트4'},
          ]};
  }
}

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
  border: 1px solid black;
  margin-top:0.5vh;
  background-color:#fff;
}
</style>