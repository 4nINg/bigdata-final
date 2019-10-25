<template>
  <div>
    <NavigationBar />
    <UserRank />
    <NewProduct />
    <EventBanner />
    <Function />
    <Footer />
  </div>
</template>
<script>
import NavigationBar from "../../Base/NavigationBar";
import UserRank from "../Panel/UserRank";
import NewProduct from "../Panel/NewProduct";
import EventBanner from "../Panel/EventBanner";
import Function from "../Panel/Function";
import Footer from "../../Base/Footer";

export default {
  components: {
    NavigationBar: NavigationBar,
    UserRank: UserRank,
    NewProduct: NewProduct,
    EventBanner: EventBanner,
    Function: Function,
    Footer: Footer
  },
  data: () => ({}),
  methods: {}
};
</script>
<style>
</style>