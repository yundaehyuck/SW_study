<template>
  <div id="app">
    <h1 class="text-center">Coffee Order App</h1>
    <div class="container d-flex flex-column">
    <div class="container d-flex justify-content-between">
    <div class="drink mx-auto">
    <MenuList/>
    </div>
    <div class="size mx-auto">
    <SizeList/>
    </div>
    </div>
    <button @click="click_order">장바구니 담기</button>
    <OrderList/>
  </div>
  
  </div>
</template>


<script>

import MenuList from '@/components/MenuList.vue'
import SizeList from '@/components/SizeList.vue'
import OrderList from '@/components/OrderList.vue'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
  },
  methods: {
    click_order() {
      this.$store.dispatch('orderBag')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
