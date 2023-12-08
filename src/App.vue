<template>
  <div class="container">
    <HeaderItem></HeaderItem>
  </div>
</template>

<script>
import HeaderItem from './components/header.vue';


export default {
  name: 'App',
  components: {
    HeaderItem
  },
}
</script>

<style>
body {
  background-color: black;
}
</style>
