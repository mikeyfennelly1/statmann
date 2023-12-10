<template>
  <div style="font-family: SmoochSans; color: white;" class="bg-dark text-SmoochSans ">
    <NavbarItem></NavbarItem>
    <HeaderItem></HeaderItem>
    <ChartOne></ChartOne>
    <SidebarItem></SidebarItem>
  </div>
</template>

<script>
import HeaderItem from './components/header.vue';
import NavbarItem from './components/navbar.vue'
import ChartOne from './components/chart1.vue';
import SidebarItem from './components/sidebar.vue'



export default {
  name: 'App',
  components: {
    NavbarItem,
    HeaderItem,
    ChartOne,
    SidebarItem,
  },
}
</script>

<style>
</style>