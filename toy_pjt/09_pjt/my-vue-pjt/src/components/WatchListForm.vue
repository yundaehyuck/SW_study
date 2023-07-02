<template>
  <div id="watch-list-form">
    <input 
        type="text"
        v-model.trim="inputData"
    >
    <button @click="addMovie" type="button" class="btn btn-outline-secondary btn-sm">Add</button>
  </div>
</template>

<script>
export default {
    name: "WatchListForm",
    data() {
        return {
            inputData: null
        }
    },
    methods: {
        addMovie() {
            if (!this.inputData) {
                alert("영화 제목을 입력해주세요!")
                return
            }
            this.$store.dispatch("addMovie", this.inputData)
            this.inputData = null
        }
    }
}
</script>

<style>
</style>