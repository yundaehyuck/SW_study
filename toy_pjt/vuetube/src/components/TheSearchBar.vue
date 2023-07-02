<template>
    <div>
    <input type="text" v-model="search" @keyup.enter="searchVideo">
    </div>

</template>

<script>

export default {

    data: function() {

        return {

            search: '',
        }
    },

    methods: {

        searchVideo: function(){

            this.$emit('search-video',this.search)

        }
    }
}
</script>

<style>
input {
    width:1480px;
    height:50px;
}
</style>