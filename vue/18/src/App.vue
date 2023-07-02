<template>
  <div id="app">
    <h1>Todo List</h1>
    <div class="form">
    <select v-model="select">
      <option value="" selected="selected">전체</option>
      <option value="doing">진행중</option>
      <option value="complete">완료</option>
    </select>
    &nbsp;
    <input type="text" v-model.trim="text">
    &nbsp;
    <button @click="createTodo">+</button>
    </div>

    <div v-if="select===''">
    <ul v-for="(todo,index) in text_list" :key="index">
      <li><input type="checkbox" class="check" @click="completeTodo(index)" :checked="todo.checked"><span class="todo" :class="{'complete':todo.isCompleted}">{{todo.text}}</span></li>
    </ul>
  </div>
  <div v-else-if="select==='doing'">
    <ul v-for="(todo,index) in text_list" :key="index">
      <li v-if="todo.isCompleted === false"><input type="checkbox" class="check" @click="completeTodo(index)" :checked="todo.checked"><span class="todo" :class="{'complete':todo.isCompleted}">{{todo.text}}</span></li>
    </ul>
  </div>
  <div v-else-if="select==='complete'">
    <ul v-for="(todo,index) in text_list" :key="index">
      <li v-if="todo.isCompleted === true"><input type="checkbox" class="check" @click="completeTodo(index)" :checked="todo.checked"><span class="todo" :class="{'complete':todo.isCompleted}">{{todo.text}}</span></li>
    </ul>
  </div>
    <br>
    <button @click="deleteTodo">완료된 할 일 지우기</button>
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
      select:''
    }
  },
  methods: {
    saveTodoToLocalStorage(context) {
      const jsonTodos = JSON.stringify(context)
      localStorage.setItem('todos',jsonTodos)
    },
    loadTodo(){

      const localStorageTodos = localStorage.getItem('todos')

      const parsedTodos = JSON.parse(localStorageTodos)

      this.text_list = parsedTodos

    },
    createTodo() {
      if (this.text) {

        const todo = {}

        todo.text = this.text
        todo.isCompleted = false
        todo.checked = false

        this.text_list.push(todo)

      } else {
        alert("내용을 입력해주세요!")
      }
      this.text=''

      this.saveTodoToLocalStorage(this.text_list)
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

      this.saveTodoToLocalStorage(this.text_list)
    },
    completeTodo(index) {
      
      this.text_list[index].isCompleted = !this.text_list[index].isCompleted
      this.text_list[index].checked = this.text_list[index].isCompleted


      this.saveTodoToLocalStorage(this.text_list)

    },
  },

  created() {
    this.loadTodo()
    //최초 비어있을때... load하는 경우 null이 되네
    if (this.text_list === null){
      this.text_list = []
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
