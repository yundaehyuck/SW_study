<template>
  <div id="watch-list-view">
    <ul class="list-group list-container">
      <li class="list-group-item color">
        <h3>보고 싶은 영화</h3>
        <WatchListForm/>
      </li>

      <WatchListItem
          v-for="(wish, index) in wishList"
          :key="index"
          :wish="wish"
        />

    </ul>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm';
import WatchListItem from '@/components/WatchListItem';

export default {
    name: "WatchListView",
    components: {
        WatchListForm,
        WatchListItem
    },
    computed: {
      wishList() {
        return this.$store.state.wishList
      }
    }
}
</script>

<style>
.color {
  background-color: rgba(153, 204, 255, 0.3);
  padding: 30px;
}
.list-container {
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}
</style>