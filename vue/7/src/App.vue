<template>
  <div id="app">
    <header class="title">
    <h1>캐릭터 진화 단계 가이드</h1>
    <div class="buttonRow">
      <div v-on:click="clickHome()" class="button">
        <span>Home</span>
      </div>
      <div v-on:click="clickStart()" class="button">
        <span>Start</span>
      </div>
    </div>
  </header>
  <div v-if="isStarted===false">
    <h2>Start버튼으로 시작해 보세요!</h2>
    <img src="./assets/ssafy-banner.png">
  </div>
  <div v-else>
    <Nocolor v-if="page===1" @click-left="getData" @click-right="getData" :page="page" :is-started="isStarted"/>
    <Ssafling v-else-if="page===2" @click-left="getData" @click-right="getData" :page="page" :is-started="isStarted"/>
    <Ssafleaf v-else-if="page===3" @click-left="getData" @click-right="getData" :page="page" :is-started="isStarted"/>
    <Ssaflower v-else @click-left="getData" @click-right="getData"  :page="page" :is-started="isStarted"/>
  </div>
  </div>
</template>

<script>
//생성한 하위 컴포넌트 등록
import Nocolor from './components/Nocolor.vue'
import Ssafling from './components/Ssafling.vue'
import Ssafleaf from './components/Ssafleaf.vue'
import Ssaflower from './components/Ssaflower.vue'

export default {
  name: 'App',
  components: {
    Nocolor,
    Ssafling,
    Ssafleaf,
    Ssaflower
  },
  data: function() {
    return {
      page:1,
      isStarted:false
    }
  },
  methods: {

    clickHome() {
      this.isStarted = false
      this.page = 1

      console.log(this.page)
      console.log(this.isStarted)
      
    },
    clickStart() {
      this.isStarted = true
      console.log(this.page)
      console.log(this.isStarted)
    },
    getData(a,b) {
      
      this.page = a
      this.isStarted = b

    }
  }
}
</script>

<style>


#app {
  font-family: "Noto Sans KR";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.buttonRow {
  display: flex;
  justify-content:center;
  width:600px;
  height: 80px;
  margin-left:auto;
  margin-right:auto;
}

.button {
display: flex;
align-items: center;
justify-content: center;
border: 1px solid #FBB117;
width:100px;
height:50px;
margin-left:15px;
margin-right:15px;
}

.button:hover {
      background-color: #FBB117;
    }

.title {
  display:flex;
  flex-direction: column;
  text-align: center;
}


</style>
