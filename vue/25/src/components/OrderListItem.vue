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
    <div class="price">
    <p>{{`가격: ${totalPrice}원`}}</p>
    <p>{{`${order.option[0].type} ${order.option[0].count}회 | ${order.option[1].type} ${order.option[1].count}회 | ${order.option[2].type} ${order.option[2].count}회 |`}}</p>
  </div>
  <button @click="removeOrder(index)">삭제</button>
  </div>
  </div>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
    index: Number,
  },
  computed: {
    totalPrice: function () {

      let total = 0

      for(let i=0; i<3; i++){

        total += this.order.option[i].price * this.order.option[i].count
      }
      
      return total + this.order.menu.price + this.order.size.price
    }
  },
  methods: {
    removeOrder: function(index) {

      this.$emit('remove-order',index)

    }
  }
}
</script>

<style>
</style>