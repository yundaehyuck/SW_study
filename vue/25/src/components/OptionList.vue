<template>
  <div>
    <h1>3. 옵션을 고르세요.</h1>
    <ul class="option-list">
      <OptionListItem
      v-for="(option,index) in optionList"
      :key="index"
      :option="option"
      @decrease="decrease"
      @increase="increase"
      />
    </ul>
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem.vue'

export default {
  name: 'OptionList',
  components: {
    OptionListItem
  },
  computed: {
    optionList: function () {

      return this.$store.state.optionList
    },
  },
  methods: {
    increase: function (newOption) {

      this.$store.dispatch('updateOption',newOption)


    },
    decrease: function (newOption) {

      this.$store.dispatch('updateOption',newOption)
    },
  },
}
</script>

<style>
</style>