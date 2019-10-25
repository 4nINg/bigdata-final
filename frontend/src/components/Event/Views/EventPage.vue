<template>
  <div>
    <Navigation />
    <EventList />
  </div>
</template>
<script>
import Navigation from "../../Base/NavigationBar";
import EventList from "../Panel/EventList";

export default {
  components: {
    Navigation: Navigation,
    EventList: EventList
  }
};

</script>
<style>
</style>