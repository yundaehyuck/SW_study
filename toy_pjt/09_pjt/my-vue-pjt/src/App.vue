<template>
  <div id="app">
    <nav class="navbar mb-5">
      <div class="container-fluid">
        <a class="navbar-brand" href="/movies">
          <img src="@/assets/ssafy.png" alt="Logo" width="70" class="d-inline-block align-text-top">
        </a>
        <div class="right">
          <router-link to="/movies">Movie</router-link>
          <router-link to="/random">Random</router-link> 
          <router-link to="/watch-list">WatchList</router-link>
        </div>
      </div>
    </nav>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import _ from "lodash"

export default {
    name: "App",
    created() {
        const API_URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=fc9c1f07b9650d1ec4f98fb39efa792e&language=ko-kr&page=1"
        axios({
            method: "get",
            url: API_URL,
        })
            .then((response) => {
                this.$store.commit("BEST_MOVIE_LIST", response.data.results)
                const randomPick = _.sample(this.$store.state.bestMovieList, 1)
                this.$store.commit("SET_RANDOM_PICK", randomPick)
            })
            .catch((error) => {
                console.log(error)
            })
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: rgba(153, 204, 255, 0.3);
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.right > a {
  text-decoration: none;
  margin-left: 10px;
}
</style>
