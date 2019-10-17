<template>
  <div>
    <div class="logo">
      <span>Dodam Dodam</span>
    </div>
    <SearchBox />
    <ImageBanner />
    <Interest />
    <Ingredient />
    <NavigationBar />
    <div class="margin_div"></div>
  </div>
</template>
<script>
import SearchBox from "../SearchBox";
import NavigationBar from "../NavigationBar";
import ImageBanner from "../ImageBanner";
import Interest from "../InterestList";
import Ingredient from "../Ingredient";

export default {
  components: {
    SearchBox: SearchBox,
    NavigationBar: NavigationBar,
    ImageBanner: ImageBanner,
    Interest: Interest,
    Ingredient: Ingredient
  },
  data: () => ({}),
  methods: {}
};
</script>
<style>
.logo {
  width: 100%;
  height: 7vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5em;
}

.margin_div {
  margin-top: 8vh;
  width: 100%;
  height: 1px;
}
</style>