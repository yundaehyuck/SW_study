<template>
  <div id="app">
    <h1 class="text-center">Coffee Order App</h1>
    <div class="container d-flex justify-content-between">
    <div class="drink mx-auto">
    <MenuList/>
    </div>
    <div class="size mx-auto">
    <SizeList/>
    </div>
    </div>
  </div>
</template>


<script>

import MenuList from '@/components/MenuList.vue'
import SizeList from '@/components/SizeList.vue'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
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
