<template>
  <div id="movie-card">
    <div class="col">
        <div class="card h-100">
            <img :src="movie_url" class="card-img-top" alt="poster">
            <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
                <p class="card-text2">{{ movie.overview }}</p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "MovieCard",
    props: {
        movie: Object,
    },
    data() {
        return {
            movie_url: `http://image.tmdb.org/t/p/w185/${this.movie.poster_path}`
        }
    }
}
</script>

<style>
.card-text2 {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

#movie-card img {
    height: 35rem;
}
</style>