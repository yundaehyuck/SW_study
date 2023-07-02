<template>
  <div id="movie-view" class="d-flex flex-wrap">
    <div class="row row-cols-1 row-cols-md-3 g-4">
        <MovieCard
            v-for="movie in bestMovieList"
            :key="movie.id"
            :movie="movie"
        />
    </div>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard"

export default {
    name: "MovieView",
    components: {
        MovieCard
    },
    computed: {
        bestMovieList() {
            return this.$store.state.bestMovieList
        }
    },
}
</script>

<style>
</style>