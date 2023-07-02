<template>
    <div>
        <div class="list">
        <div v-for="(url,index) in thumbnails" :key="index">
        <div class="image d-flex my-1">
        <img :src="`${url}`" alt="">
        <p> {{ titles[index] }}</p>
        </div>
        <hr v-if="index<=2">
        </div>
        </div>
    </div>
</template>

<script>

export default {

    props: {
        thumbnails:Array,
        titles:Array,
    }
}
</script>

<style>
.list {
    border:1px solid rgba(0,0,0,0.3);
}

</style>