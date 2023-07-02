<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <MenuListItem
    v-for="(menu,index) in menuList"
    :key="index"
    :menu="menu"
    @click.native="selectedMenu(menu)"
    />
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem.vue'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList
    },
    selectedDrink: function() {
      return this.$store.state.selectedDrink
    }
  },
  methods: {
    selectedMenu(menu) {
        
      menu.selected = true

      for(const notMenu of this.menuList){

        if (notMenu.title != menu.title){

          notMenu.selected = false
        }
      }

      const is_selected = !this.selectedDrink

      this.$store.dispatch('showSize',is_selected)




      }

    },
  }

</script>

<style>

</style>