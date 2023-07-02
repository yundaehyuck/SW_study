<template>
    <div>
        <VideoListItem
        :thumbnails="thumbnailsProps"
        :titles="titlesProps"/>
    </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {

    props: {

        thumbnailsProps: Array,
        titlesProps: Array,
    },

    components: {
        VideoListItem
    }
}
</script>

<style>
</style>