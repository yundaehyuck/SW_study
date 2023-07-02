import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  getters: {
    counterDouble(state) {
      return state.counter * 2
    }
  },
  mutations: {
    INCREASE_COUNTER(state,counter){

      state.counter = counter
    },
    DECREASE_COUNTER(state,counter){
      state.counter = counter
    }
  },
  actions: {
    increase(context,counter){
      context.commit('INCREASE_COUNTER',counter)
    },
    decrease(context,counter){
      context.commit('DECREASE_COUNTER',counter)
    }
  },
  modules: {
  }
})

