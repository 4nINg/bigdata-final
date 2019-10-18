<template>
  <div>
    <Navigation />
    <EventList />
  </div>
</template>
<script>
import Navigation from "../NavigationBar";
import EventList from "../EventList";

export default {
  components: {
    Navigation: Navigation,
    EventList: EventList
  }
};
</script>
<style>
</style>