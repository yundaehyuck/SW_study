<template>
  <div class="board d-flex justify-content-between" :class="{select:menu.selected}">
    <!-- 로컬 이미지 파일 불러오기  -->
    <img :src="require(`../assets/${menu.image}`)" width="50px" height="50px"> 
    <span>{{ menu.title }}</span>
    <span>{{ `${menu.price}원` }}</span>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  }
}
</script>

<style>

.board {
  width:400px;
  height:80px;
}

.board:hover {
  background-color:bisque
}

.select {
  background-color:antiquewhite
}
</style>