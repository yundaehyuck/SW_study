<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <div v-if="this.video_id.length === 0" class="input1">
    <TheSearchBar class="mb-3"
    @search-video="getSearch"/>
    </div>
    <div v-else class="input2">
      <TheSearchBar class="mb-3"
      @search-video="getSearch"/>
    </div>
    <div class="home d-flex">
    <VideoDetail
    :video_id="video_id"/>
    <VideoList 
    :thumbnails-props="thumbnails"
    :titles-props="titles"/>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

export default {
  name: 'App',
  data: function() {

    return {

      video_id : [],
      thumbnails : [],
      titles : [],
    }
  },
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {

    getSearch: function(search) {
      
      //검색결과 갱신을 위한 초기화
      this.video_id = []
      this.thumbnails = []
      this.titles = []

      const base_url_before = "https://www.googleapis.com/youtube/v3/search?part=snippet&"
      const base_url_after = "&type=video&key=AIzaSyCG2YOmwc09NiDmO6XrjSf8NB8DQEQlMQY"

      let search_url = ""
      search_url = base_url_before+`q=${search}`+base_url_after

      axios.get(search_url)
      .then((response)=>{

        //첫번째 비디오 아이디 저장
        this.video_id.push(response.data.items[4].id.videoId)
        this.video_id.push(response.data.items[4].snippet.title)
        this.video_id.push(response.data.items[4].snippet.description)
        
        for(let i=0; i<4; i++){

          this.thumbnails.push(response.data.items[i].snippet.thumbnails.default.url)

          this.titles.push(response.data.items[i].snippet.title)

        }

      })
      .catch((error) => {
        console.log(error)
      })

    }
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
  margin-top: 60px;
}

.input1 {
  position:relative;
  top:500px;
}
</style>
