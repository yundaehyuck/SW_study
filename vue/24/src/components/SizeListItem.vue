<template>
    <div v-if="selectedDrink===true" class="board d-flex justify-content-between" :class="{select:size.selected}">
    <span>{{ size.name }}</span>
    <span>{{ `${size.price}원`}}</span>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  computed:{
    selectedDrink() {

      console.log(this.$store.state.selectedDrink)
      return this.$store.state.selectedDrink
    }
  }
}
</script>

<style>

.select {
  background-color:antiquewhite
}
</style>