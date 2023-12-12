<template>
  <div style="font-family: SmoochSans; color: black;" class="bg-dark text-SmoochSans ">
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
  // mounted() {
  //   axios.get('http://localhost:5000/videos/video2', {})
  //     .then(response => {
  //       this.message = response.data.title;
  //       console.log(`This is this.mesage: ${this.message}`)
  //     })
  //     .catch(error => {
  //       console.error('Error fetching data: ', error);
  //     });
  //   }
  }
</script>
<style>
</style>