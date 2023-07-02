import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedDrink: false,
    orderList: [],
    menuList: [
      {
        title:'콜드브루',
        price:4900,
        selected:false,
        image:'coldbrew.jpg'
      },
      {
        title:'카라멜마키아또',
        price:5900,
        selected:false,
        image:'caramelmacchiato.jpg'
      },
      {
        title:'아포가토',
        price:6100,
        selected:false,
        image:'affogato.jpg'
      }
    ],
    sizeList: [
      {
        name:'small',
        price:1500,
        selected:false
      },
      {
        name:'tall',
        price:2500,
        selected:false
      },
      {
        name:'venti',
        price:4000,
        selected:false
      }
    ],
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state){
      
      let total_price = 0

      for(const order of state.orderList){

        total_price += order.menu.price
        total_price += order.size.price
      }
      return total_price
    }
  },
  mutations: {
    SHOW_SIZE: function(state,is_select){

      state.selectedDrink = is_select

    },
    addOrder: function (state) {
      const customer_order = {}

      for(const menu of state.menuList){

        if (menu.selected === true){

          customer_order.menu = menu
        }
      }
      for(const size of state.sizeList){

        if(size.selected === true){

          customer_order.size = size
        }
      }

      state.orderList.push(customer_order)

    },
    updateMenuList: function (state,selectedMenu) {
      state.menuList.forEach(function(menu) {
        if(menu.title === selectedMenu.title){
          menu.selected = true
        }
      })
    },
    updateSizeList: function (state,selectedSize) {

      state.sizeList.forEach(function(size){

        if(size.name === selectedSize.name){
          size.selected=true
        }
      })
    },
  },
  actions: {
    showSize(context,is_select){
      context.commit('SHOW_SIZE',is_select)
    },

    orderBag(context){
      context.commit('addOrder')
    }
  },
  modules: {
  }
})
