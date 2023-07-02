<template>
    <div class="todolist">
        <h3 class="text-start ms-4 mt-3">모든 할일</h3>
        <hr>
        <div class="container d-flex flex-column">
        <div class="checkbox mt-3" v-for="(todo,index) in allToDo" :key="index">
        <div class="row1 mt-3 d-flex justify-content-between">
        <div class="minibox d-flex justify-content-between">
        <i :id="`${index}`" class="mx-3 bi bi-circle fs-3 check" style="cursor: pointer;" @click="click_check(index)"></i>
        <h4 class="mt-2 text-start">{{ todo.content }}</h4>
        </div>
        <i :id="`${index}`" class="bi bi-star text-end me-3 star" style="color:yellow; font-size:2rem; cursor: pointer;" @click="click_star(index)"></i>
        </div>    
        </div>
        </div>
    </div>
</template>

<script>

export default {

    data: function() {

        return {

            click_count : 0,
            is_clicked: false,
            Active:true,
        }
    },

    computed: {

        allToDo() {

            return this.$store.state.todo.list
        }
    },

    methods:{
        click_star(index) {

            const star = document.querySelectorAll('.star')

            for(const point of star){

                if(Number(point.id) === index) {

                    if (point.classList.contains('bi-star-fill') === false){

                    point.classList.add('bi-star-fill')
                    point.classList.remove('bi-star')

                    } else {

                    point.classList.remove('bi-star-fill')
                    point.classList.add('bi-star')

                    }

                }


            }

        },

        click_check(index){

            const check = document.querySelectorAll('.check')

            for(const point of check){

                if(Number(point.id)===index){

                    if (point.classList.contains('bi-check-circle') === false){

                        point.classList.add('bi-check-circle')
                        point.classList.remove('bi-circle')

                    } else {

                        point.classList.add('bi-circle')
                        point.classList.remove('bi-check-circle')
                    }
                }
            }
        }
    }


}


</script>

<style>
.todolist {
    border:1px solid black;
    border-radius:10px;
    width:1000px;
    height:500px;
}

.checkbox {
    border:0.1px solid rgba(0, 0, 0, .1); 
    border-radius:10px;
    height:80px;
}
</style>