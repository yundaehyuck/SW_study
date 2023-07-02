<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  methods: {
    increase: function () {
      this.$store.state.counter += 1
      this.$store.dispatch('increase',this.$store.state.counter)
    },
    decrease: function () {
      this.$store.state.counter -= 1
      this.$store.dispatch('decrease',this.$store.state.counter)
    },
  },
  computed: {
    counter() {
      return this.$store.state.counter
    },
    counterDouble() {
      return this.$store.getters.counterDouble
    }
  },
}
</script>

<style>
</style>