import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title:'콜드브루',
        price:4900,
        selected:false,
        image:'src/assets/coldbrew.jpg'
      },
      {
        title:'카라멜마키아또',
        price:5900,
        selected:false,
        image:'src/assets/caramelmacchiato.jpg'
      },
      {
        title:'아포가토',
        price:6100,
        selected:false,
        image:'src/assets/affogato.jpg'
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
  },
  mutations: {
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
  },
  modules: {
  }
})
