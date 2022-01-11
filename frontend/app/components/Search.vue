<template>
  <div class="sm:pt-0"><div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
      <div class="mt-8 bg-white overflow-hidden shadow sm:rounded-lg p-6">
        <input type="search"
               class="flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
               placeholder="Поиск"
               v-model="search"
        />
        <p class="mt-3 text-gray-600">{{ infoText }}</p>

        <div class="mt-6 p-3 bg-gray-100" v-for="s in searchResults">
          <p class="mt-3 text-gray-600" v-html="s.highlighted"></p>
          <p>{{s.code}}</p>
          <p>{{s.disease_description}}</p>
          <p>{{s.parent_code}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NuxtTutorial',
  data: () => ({
    search: '',
    searchResults: null,
    infoText: null,
    cancelSource: null,
  }),

  methods: {

    async fetchSearch() {
      this.searchResults = null
      this.infoText = 'Поиск...'

      this.cancelSearch()
      this.cancelSource = this.$axios.CancelToken.source();

      const search = await this.$axios.$get(
        'icd_codes/',
        {
          params: {
            search: this.search
          },
          cancelToken: this.cancelSource.token
        })
      this.searchResults = search.results
      this.infoText = null;
      this.cancelSource = null;
    },

    cancelSearch() {
      if (this.cancelSource) {
        this.cancelSource.cancel()
      }
    }

  },
  watch: {
    search: function (value) {
      this.fetchSearch();
    }
  }
}
</script>

<style>

.highlighted {
  color: deeppink;
  background-color: pink;
  font-weight: 400;
}

</style>
