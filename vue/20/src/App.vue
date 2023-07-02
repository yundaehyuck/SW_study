<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="wrap">
    <h2>예약페이지</h2>
    <h3>시간 선택</h3>
    <span v-for="(time,index) in times" :key="index" v-on:click="click_button(index)" :class="{selected:Active[index]}">{{ time }}&nbsp;<p v-if="(index+1)%8===0"></p></span>
  </div>
    <hr>
    <h3>선택 시간:&nbsp;
      <span v-for = "index in selected_time" :key="index" :v-text="times">{{times[index]}}&nbsp;</span>
    </h3>
  
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>

<script>

export default {
  name: 'App',
  components: {
  },
  data : function() {
    
    //30분 단위로 00:00~23:30까지 시간데이터를 생성함
    let time_list = []
    let active_list = []

    var h = 0
    var i = 0

    while(true){

      i++

      if (i % 2 == 1){

        if(h<=9){
          time_list.push(String(0)+String(h)+":00")
        } else {
          time_list.push(String(h)+":00")
        }

      } else {
        if(h<=9){
          time_list.push(String(0)+String(h)+":30")
        } else {
          time_list.push(String(h)+":30")
        }
        h++
      }

      if(h==24){
        break;
      }

      active_list.push(false)

      

    }

    return {
      times : time_list,
      Active:active_list,
      selected_time:[],
    }
  },
  methods: {
    click_button(index) {

        this.$set(this.Active,index,!this.Active[index])

        if(this.Active[index] === true){
          if (this.selected_time.length >=5){
            this.$set(this.Active,index,!this.Active[index])
            alert('5타임까지만 신청할 수 있습니다.')
            return;
          }
          this.selected_time.splice(index,0,index)
        } else {
          this.selected_time = this.selected_time.filter((element) => element !== index);
        }

        //숫자정렬할때, sort()하면 안됨
        //.sort(function(a,b){return a-b})로 해줘야함

        this.selected_time = this.selected_time.sort(function(a,b) { return a-b })

        if (this.selected_time.length === 5){
        alert('5타임까지만 신청할 수 있습니다.')
        return;
        }



    }
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif,'Noto Sans KR';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.selected {

  background-color: #658dc63d;
}

.wrap {
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px,
    rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  width: 520px;
  margin: 0 auto;
}

</style>
