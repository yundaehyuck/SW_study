<template>
    <div class="todolist">
        <h3 class="text-start ms-4 mt-3">중요 할일</h3>
        <div class="work">
        <div class="new d-flex">
            <h3 @click="addImportant()" class="mx-4">+</h3>
            <input type="text" placeholder="할 일을 작성해주세요!" v-model="text" class="me-3">
        </div>
        <hr>
        <div class="container d-flex flex-column mb-3">
        <div class="mt-3" v-for="(todo,index) in allToDo" :key="index">
        <div class="checkbox row1 d-flex justify-content-between" v-if="todo.isImportant===true &&todo.isCompleted===false">
        <div class="minibox d-flex justify-content-between">
        <i :id="`${index}`" class="mx-3 bi fs-3" :class="{'bi-check-circle':todo.isCompleted, 'bi-circle':!todo.isCompleted}" style="cursor: pointer;" @click="click_check(index)"></i>
        <h4 class="mt-2 text-start">{{ todo.content }}</h4>
        </div>
        <i :id="`${index}`" class="bi text-end me-3" :class="{'bi-star-fill':todo.isImportant,'bi-star':!todo.isImportant}" style="color:yellow; font-size:2rem; cursor: pointer;" @click="click_star(index)"></i>
        </div>    
        </div>
        </div>
        </div>
    </div>
</template>

<script>

export default {

    data: function() {

        return {

            text:'',
        }
    },

    computed: {

        allToDo() {

            return this.$store.state.todo.list
        }
    },

    methods:{

        addImportant(){

            this.$store.dispatch('todo/addImportant',this.text).todo

        },
        click_star(index) {

        this.$store.dispatch('todo/changeImportant',index).todo

        },

        click_check(index){

        this.$store.dispatch('todo/changeToday',index).todo
        }
    }


}


</script>

<style scoped>
.todolist {
    border:1px solid black;
    border-radius:10px;
}

.checkbox {
    border:0.1px solid rgba(0, 0, 0, .1); 
    border-radius:10px;
}

input {
    border:0.1px solid rgba(0, 0, 0, .1); 
    border-radius:10px;
    width:900px;
}
</style>