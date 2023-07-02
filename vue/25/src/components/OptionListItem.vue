<template>
  <div>
    <div class="board d-flex justify-content-between">
      <span>{{ option.type }}</span>
    <div class="choice">
     <button @click="decrease(option)">-</button>
     <span class="my-auto">{{ option.count }}</span>
     <button @click="increase(option)">+</button>
    </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  computed: {

    selectedOption() {
      return this.$store.state.selectedOption
    }
  },
  methods: {
    increase(option) {

      option.count += 1

      this.$emit('increase',option)
    },
    decrease(option) {

      if(option.count > 0) {
        
        option.count -= 1
      }

      this.$emit('decrease',option)
    },
  },
}
</script>

<style>
</style>