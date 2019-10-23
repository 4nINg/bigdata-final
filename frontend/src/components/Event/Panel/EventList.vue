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