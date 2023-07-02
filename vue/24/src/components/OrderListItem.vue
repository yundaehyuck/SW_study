<template>
  <div>
    <div class="container d-flex justify-content-between">
    <div class="order d-flex">
    <img :src="require(`../assets/${order.menu.image}`)" width="50px" height="50px">
    <div>
      <p>{{order.menu.title}}</p>
      <p>{{`사이즈:${order.size.name}`}}</p>
    </div>
    </div>
    <span>{{`가격: ${totalPrice}원`}}</span>
  </div>
  </div>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      
      return this.order.menu.price + this.order.size.price
    },
  },
}
</script>

<style>
</style>