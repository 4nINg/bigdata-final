<template>
  <div class="searchpage_main">
    <div class="searchpage_input">
      <input type="text" placeholder="제품명, 성분명, 브랜드명을 검색하세요." v-model="keyword" id="search" />
      <i class="fas fa-search" aria-hidden="true" />
    </div>
    <div class="current_keyword">
      <div class="current_keyword_header">
        <span>최근 검색어</span>
      </div>
      <div></div>
    </div>
  </div>
</template>
<script>
import { mapActions } from "vuex";
import router from "../../../router";
export default {
  data: () => ({
    keyword: ""
  }),
  mounted() {
    document.getElementById("search").addEventListener("keypress", e => {
      if (e.which == 13) {
        this.searchByKeyword(this.keyword);
        router.push("searchResult");
      }
    });
  },
  methods: {
    ...mapActions("data", ["searchByKeyword"])
  }
};
</script>