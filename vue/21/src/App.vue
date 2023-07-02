<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div class="container">
    <div class="wrap">
    <div class="left">
      <h2>예약 페이지</h2>
      <h3>선생님 선택</h3>
      <div class="buttonRow">
      <div v-on:click="click_teacher(1)" class="button" :class="{selected:Active_teacher[1]}">
      <span>Eric</span>
      </div>
      <div v-on:click="click_teacher(2)" class="button" :class="{selected:Active_teacher[2]}">
      <span>Tony</span>
      </div>
    
      </div>
      <hr>
      <h3>시간 선택</h3>
      <span v-for="(time,index) in times" :key="index" v-on:click="click_time(index)" :class="{selected:Active[index]}">{{ time }}&nbsp;<p v-if="(index+1)%6===0"></p></span>

    </div>
    <div class="right">
      <h2>상담 신청 현황</h2>
      <h3>상담 선생님</h3>
      <span>성함 :&nbsp;
      <span :v-text="selected_name">{{selected_name}}</span>
    </span>
      <hr>
      <h3>예약 현황</h3>
      <span>시간들 :&nbsp;
      <span v-for = "index in selected_time" :key="index">{{times[index]}}&nbsp;</span>
    </span>
      <hr>
      <img alt="Vue logo" src="./assets/ssafy-logo.png">
    </div>
  </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  data: function() {

    return {
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30",
  "12:00","12:30","13:00","13:30","14:00","14:30",
  "15:00","15:30","16:00","16:30","17:00","17:30",
],
    selected_time:[],
    Active:[false,false,false,false,false,false,
            false,false,false,false,false,false,
            false,false,false,false,false,false,],
    
    selected_name:'',
    Active_teacher:[false,false,false],
    id:0,
    }
  },
  methods: {
    click_time(index) {

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
    },
    click_teacher(id) {

      this.$set(this.Active_teacher,id,!this.Active_teacher[id])

      if(id === 1){

        if(this.Active_teacher[2]===true){
          this.$set(this.Active_teacher,2,false)
        }
        
        if(this.Active_teacher[id]===true){
          this.selected_name = "Eric"
        } else if(this.Active_teacher[id]===false){
          this.selected_name=""
        }
      } else {

        if(this.Active_teacher[1]===true){
          this.$set(this.Active_teacher,1,false)
        }

        if(this.Active_teacher[id]===true){
        this.selected_name = "Tony"
        }else if(this.Active_teacher[id]===false){
          this.selected_name=""
        }
      } 
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
.container {
  display:flex;
  justify-content:center;
}

/* 왼쪽 오른쪽 균일하게 나누기 */
.wrap {
  display:flex;
  flex-direction:row;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px,
    rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;

  width:800px;
  height:400px;
}

/* 크기 강제 고정 */
.left {
  width:400px;
}
.right {
  width:400px;
  background-color: #658dc63d;
}

.buttonRow {
  display:flex;
  justify-content: space-evenly;
}

.button {

  display: flex;
  align-items: center;
  justify-content: center;
  width:20%;
  height:30px;
  border: 1px solid #0F4C81;
}

.button:hover {
  background-color:#658dc63d;
}

.selected {
  background-color: #658dc63d;
}
</style>
