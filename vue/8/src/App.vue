// App.vue

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
      this.counter += 1
      this.$store.dispatch('increase',this.counter)
    },
    decrease: function () {
      this.counter -= 1
      this.$store.dispatch('decrease',this.counter)
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