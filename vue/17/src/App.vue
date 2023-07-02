<template>
  <div id="app">
    <h1>Todo List</h1>
    <div class="form">
    <input type="text" v-model.trim="text">
    &nbsp;
    <button @click="createTodo">+</button>
    </div>
    <ul v-for="(todo,index) in text_list" :key="index">
      <li><input type="checkbox" class="check" @click="completeTodo(index)"><span class="todo" :class="{'complete':todo.isCompleted}">{{todo.text}}</span></li>
    </ul>
    <br>
    <button @click="deleteTodo">완료 목록 삭제</button>
  </div>
</template>

<script>

export default {
  name: 'App',
  components:{
  },
  data: function() {
    return {
      text: '',
      text_list:[],
    }
  },
  methods: {
    createTodo() {
      if (this.text) {

        const todo = {}

        todo.text = this.text
        todo.isCompleted = false

        this.text_list.push(todo)

      } else {
        alert("내용을 입력해주세요!")
      }
      this.text=''
    },
    deleteTodo() {
      
      const new_text_list = []

      for(const todo of this.text_list){

        if (todo.isCompleted === false){
          new_text_list.push(todo)
        }
      }

      this.text_list = new_text_list

      const checkbox = document.querySelectorAll('.check')

      for(const check of checkbox){
        check.checked = false
      }
    },
    completeTodo(index) {
      
      this.text_list[index].isCompleted = !this.text_list[index].isCompleted

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
}

.complete {
  text-decoration: line-through;
}
</style>
