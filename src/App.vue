<template>
  <div style="font-family: SmoochSans; color: white;" class="bg-dark text-SmoochSans ">
    <NavbarItem></NavbarItem>
    <HeaderItem></HeaderItem>
    <ChartOne></ChartOne>
  </div>
</template>

<script>
import HeaderItem from './components/header.vue';
import NavbarItem from './components/navbar.vue'
import ChartOne from './components/chart1.vue';


export default {
  name: 'App',
  components: {
    NavbarItem,
    HeaderItem,
    ChartOne,
  },
}
</script>

<style>
</style>