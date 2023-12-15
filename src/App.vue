<template>
  <div style="font-family: Afacad; color: white;" class="bg-dark text-SmoochSans ">
    <NavbarItem></NavbarItem>
    <HeaderItem></HeaderItem>
    <ChartOne></ChartOne>
    <SidebarItem></SidebarItem>
    <SearchBarItem></SearchBarItem>
  </div>
</template>

<script>
import HeaderItem from './components/header.vue';
import NavbarItem from './components/navbar.vue'
import ChartOne from './components/chart1.vue';
import SidebarItem from './components/sidebar.vue'
import SearchBarItem from './components/SearchBarItem.vue'

// import axios from 'axios'



export default {
  name: 'App',
  components: {
    NavbarItem,
    HeaderItem,
    ChartOne,
    SidebarItem,
    SearchBarItem,
  },
}
</script>
<style >
</style>