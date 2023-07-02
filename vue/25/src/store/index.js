import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedDrink: false,
    selectedOption: false,
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
    optionList:[
      {
        type: '샷 추가',
        price: 1000,
        count: 0,
      },
      {
        type: '바닐라 시럽',
        price: 1500,
        count: 0,
      },
      {
        type: '아이스크림 추가',
        price: 2000,
        count: 0,
      }

    ]
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

        for(let i=0; i<3; i++){
        
          total_price += order.option[i].price * order.option[i].count
        
        }

      }

      return total_price
    },
  },
  mutations: {
    SHOW_SIZE: function(state,is_select){

      state.selectedDrink = is_select

    },
    SHOW_OPTION: function(state,is_select){
      state.selectedOption = is_select
    },
    addOrder: function (state) {

      const customer_order = {}

      for(const menu of state.menuList){

        if (menu.selected === true){

          const copymenu = _.cloneDeep(menu)

          customer_order.menu = copymenu

          menu.selected = false //장바구니에 담았으면 초기화
        }
      }
      for(const size of state.sizeList){

        if(size.selected === true){

          const copysize = _.cloneDeep(size)

          customer_order.size = copysize

          size.selected = false //장바구니에 담았으면 초기화
        }
      }
      //깊은 복사를 수행하여, 변경되는 것을 방지함
      const copyoption = _.cloneDeep(state.optionList)

      customer_order.option = copyoption

      state.orderList.push(customer_order)

      //모든 값들을 초기화

      for(const option of state.optionList){
        option.count = 0
      }

      state.selectedDrink = false
      state.selectedOption = false

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
    updateOptionList: function(state,newOption){

      state.optionList.forEach(function(option){

        if(option.type === newOption.type){

          option.count = newOption.count
        }
      })
    },
    REMOVE_ORDER: function(state,index){
      
      state.orderList.splice(index,1)

    }
  },
  actions: {
    showSize(context,is_select){
      context.commit('SHOW_SIZE',is_select)
    },
    showOption(context,is_select){
      context.commit('SHOW_OPTION',is_select)
    },
    orderBag(context){
      context.commit('addOrder')
    },

    updateOption(context,newOption){
      context.commit('updateOptionList',newOption)
    },
    removeOrder(context,index){
      context.commit('REMOVE_ORDER',index)
    }
  },
  modules: {
  }
})
