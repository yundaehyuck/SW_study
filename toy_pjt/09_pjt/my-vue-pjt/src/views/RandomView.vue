<template>
  <div id="random-view">
    <div class="row row-cols-1 row-cols-md-3 g-4 d-flex justify-content-center">
        <div class="col">
            <button class="btn btn-success mb-4" @click="pickMovie">PICK</button>
            <div class="card">
                <img :src="randomPickUrl" class="card-img-top" alt="random-url">
                <div class="card-body">
                    <h5 class="card-title">{{ randomPick.title }}</h5>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import _ from "lodash"
// import axios from "axios"

export default {
    name: "RadomVIew",
    computed: {
        bestMovieList() {
            return this.$store.state.bestMovieList
        },
        randomPick() {
            return this.$store.state.randomPick
        },
        randomPickUrl() {
            return `http://image.tmdb.org/t/p/w185/${this.$store.state.randomPick.poster_path}`
        }
    },
    methods: {
        pickMovie() {
            const randomPick = _.sample(this.$store.state.bestMovieList, 1)
            this.$store.commit("SET_RANDOM_PICK", randomPick)
        }
        // pickMovie() {
        //     axios({
        //         methods: 'get',
        //         url: "https://api.openweathermap.org/data/2.5/weather?q=Gwangju,kor&appid=48cbd49bbb4ddec293922944bcb7886a"
        //     })
        //       .then((response)=> {
        //         console.log(response)
        //       })
        //       .catch((error)=>{
        //         console.log(error)
        //       })
        // }
    },
}
</script>

<style>
#random-view button {
    width: 100%;
}
</style>