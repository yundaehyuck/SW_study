<template>
  <li class="list-group-item list-group-item-light" id="watch-list-item" :class="{cancel : wish.isCancel}" @click="doCancel">
   {{ wish.title }}
  </li>
</template>

<script>
export default {
    name: "WatchListItem",
    props: {
      wish: Object
    },
    methods: {
      doCancel() {
        this.$store.dispatch("doCancel", this.wish)
      }
    }
}
</script>

<style>
.cancel {
  text-decoration: line-through;
  background: #f1f3f5;
  color: gray;
}
</style>