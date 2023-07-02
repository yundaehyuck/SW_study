<template>
  <div>
    <h1>주문 내역</h1>
    <p>{{ `총 ${totalOrderCount}건: ${totalOrderPrice}원`}}</p>
    <OrderListItem
    v-for="(order,index) in orderList"
    :key="index"
    :order="order"
    :index="index"
    @remove-order="removeOrderList"
    />
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem.vue'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList: function () {
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },
  methods: {
    removeOrderList: function(index) {

      this.$store.dispatch('removeOrder',index)



    }
  }
}
</script>

<style>
</style>