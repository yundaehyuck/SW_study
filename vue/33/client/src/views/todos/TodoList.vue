<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id" :id="`todo-${todo.id}`">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ 'is-completed': todo.is_completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  methods: {
    getTodos: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
      })
        .then(res => {
          console.log(res)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      // 3번 문제

      const liTag = document.querySelector(`#todo-${todo.id}`)

      const ID = todo.id

      axios({

        method:'delete',
        url:`http://127.0.0.1:8000/todos/${ID}`,

      })
      .then(()=>{

        liTag.remove()

      })
      .catch((err)=>{
        console.log(err)
      })
    },

    updateTodoStatus: function (todo) {
      // 4번 문제
      console.log(todo)
      
      const ID = todo.id
      const title = todo.title
      const is_completed = !todo.is_completed

      axios({
        method:'put',
        url:`http://127.0.0.1:8000/todos/${ID}/`,
        data:{title, is_completed} //put은 모든 필드를 수정함
      })
      .then((res) => {

        console.log(res)

        // todo.title = title
        todo.is_completed = is_completed

      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
