<template>
    <div class="ssafling">
    <div class="wrap">
        <h2>1단계</h2>
        <div class="arrImgRow">
        <div v-on:click="clickLeft()" class="arrow-prev">
            <span></span>
        </div>
        <img src="../assets/saffling.png">
        <div v-on:click="clickRight()" class="arrow-next">
            <span></span>
        </div>
        </div>
        <h2>싸플링</h2>
    </div>
</div>

</template>

<script>
export default {
    name: 'Ssafling',
    props:{
        page:Number,
        isStarted:Boolean,
    },
    methods: {
        clickLeft() {

            if (this.page === 1){

                this.isStarted = false

            } else {
                this.page = this.page - 1
            }

            this.$emit('click-left',this.page,this.isStarted)


        },
        clickRight() {

            if (this.page === 4) {
                alert('Home으로 돌아갑니다!')
                this.page = 1
                this.isStarted=false
            } else {
                this.page++
            }

            this.$emit('click-right',this.page,this.isStarted)
        }

    }
}
</script>

<style scoped>

img {

width: 300px;
height: 300px;
}

.wrap {
 display:flex;
 flex-direction: column;
 justify-content: space-evenly;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px,
    rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  margin: 0 auto;
  width:600px;
}
.arrImgRow {
    display:flex;
    justify-content: space-between;
    
}

.arrow-prev,
.arrow-next {
    position: relative;
    float:left;
    border:1px solid #000;
    background-color:black;
    width:30px;
    height:30px;
    margin-top:auto;
    margin-bottom:auto;
    margin-right:20px;
    margin-left:20px;
    border-radius: 15px;
}

.arrow-prev::after {
    position: absolute;
    left: 10px; 
    top: 9px;
    content: '';
    width: 10px; /* 사이즈 */
    height: 10px; /* 사이즈 */
    border-top: 5px solid white; /* 선 두께 */
    border-right: 5px solid white;  /* 선 두께 */
    transform: rotate(225deg); /* 각도 */
}

.arrow-next::after {
    position: absolute;
    left: 6px; 
    top: 8px; 
    content: '';
    width: 10px; /* 사이즈 */
    height: 10px; /* 사이즈 */
    border-top: 5px solid white; /* 선 두께 */
    border-right: 5px solid white; /* 선 두께 */
    transform: rotate(45deg); /* 각도 */
}

</style>