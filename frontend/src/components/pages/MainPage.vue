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
import NavigationBar from "../NavigationBar";
import UserRank from "../UserRank";
import NewProduct from "../NewProduct";
import EventBanner from "../EventBanner";
import Function from "../Function";
import Footer from "../Footer";

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