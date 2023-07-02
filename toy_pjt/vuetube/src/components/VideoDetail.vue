<template>
  <div v-if="video_id[0]">
  <iframe id="ytplayer" type="text/html" width="640" height="360"
  :src="`https://www.youtube.com/embed/${video_id[0]}`"
  frameborder="0"></iframe>
  <h2>{{ video_id[1] }}</h2>
  <hr>
  <span>{{ video_id[2]}}</span>
  </div>
</template>

<script>

export default {

    props: {
        video_id:Array,
    }
}
</script>

<style>
</style>