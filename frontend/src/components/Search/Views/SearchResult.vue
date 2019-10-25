<template>
  <div class="search_result_main">
    <div class="search_result_container">
      <SearchBox />

      <div v-for="(result, index) in searchResultSliced" :key="index" class="line">
        <Product
          :ranking="-1"
          :image_url="result.image_url"
          :company_name="result.company_name"
          :name="result.name"
          :rating="-1"
        />
      </div>
    </div>
    <div class="pagination_div">
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </div>
  </div>
</template>
<script>
import Product from "../../Base/Product";
import SearchBox from "../../Base/SearchBox";
import { mapState } from "vuex";

export default {
  components: {
    Product: Product,
    SearchBox: SearchBox
  },
  data: () => ({
    cardsPerPage: 6,
    page: 1
  }),
  computed: {
    ...mapState({
      searchResult: state => state.data.searchResult
    }),
    searchResultSliced() {
      return this.searchResult.slice(
        this.cardsPerPage * (this.page - 1),
        this.cardsPerPage * this.page
      );
    },
    maxPages: function() {
      return Math.floor(
        (this.searchResult.length + this.cardsPerPage - 1) / this.cardsPerPage
      );
    }
  }
};
</script>
<style>
.search_result_main {
  width: 100%;
  min-height: 92.5vh;
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  background-color:#fff;
}


.search_result_container{
  width: 100%;
  height: 90%;
}

.search_result_container .line{
  border-top:1px solid rgb(233, 233, 233);
}

.pagination_div{
  width: 100%;
  height: 10%;
}
</style>