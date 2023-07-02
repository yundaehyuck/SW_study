<template>
  <div>
    <h1>2. 사이즈를 고르세요.</h1>
    <SizeListItem
    v-for="(size,index) in sizeList"
    :key="index"
    :size="size"
    @click.native="onSelectMenu(size)"
    />
  </div>
</template>

<script>

import SizeListItem from '@/components/SizeListItem.vue'

export default {
  name: 'SizeList',
  components: {
    SizeListItem,
  },
  computed: {
    sizeList: function () {
      return this.$store.state.sizeList
    },
    selectedOption() {
      return this.$store.state.selectedOption
    }
  },
  methods: {
    onSelectMenu: function (size) {
      size.selected = true

      for(const notSize of this.sizeList){

        if(notSize.title != size.title){
          notSize.selected = false
        }
      }

      const is_selected = !this.selectedOption

      this.$store.dispatch('showOption',is_selected)

      
    },
  },
}
</script>

<style>
</style>