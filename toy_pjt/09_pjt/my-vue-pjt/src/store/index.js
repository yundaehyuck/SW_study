import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    bestMovieList: [],
    wishList: [],
    randomPick: ""
  },
  getters: {
  },
  mutations: {
    BEST_MOVIE_LIST(state, bestMovieList) {
      state.bestMovieList = bestMovieList
      console.log(state.bestMovieList)
    },
    ADD_MOVIE(state, myWish) {
      state.wishList.push(myWish)
      console.log(state.wishList.length)
    },
    DO_CANCEL(state, myWish) {
      state.wishList = state.wishList.map((wish) => {
        if (wish === myWish) {
          wish.isCancel = !wish.isCancel
        }
        return wish
      })
    },
    SET_RANDOM_PICK(state, randomPick) {
      state.randomPick = randomPick
    }
  },
  actions: {
    addMovie(context, inputData) {
      const myWish = {
        title: inputData,
        isCancel: false 
      }
      context.commit("ADD_MOVIE", myWish)
    },
    doCancel(context, wish) {
      context.commit("DO_CANCEL", wish)
    }
  },
  modules: {
  }
})
