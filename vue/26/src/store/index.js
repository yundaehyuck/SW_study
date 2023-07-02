import Vue from 'vue'
import Vuex from 'vuex'
import toDo from '../store/modules/todo.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    toDo: {
      namespaced:true,
      toDo,
  },
}
})
