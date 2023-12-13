<template>
    <div class="container bg-primary">
        <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle">
            Dropdown button
        </button>
        <ul class="dropdown-menu">
            <li><a style="background-color: red;"  class="dropdown-item bg-secondary" href="#">Action</a></li>
            <li><a style="background-color: red;"  class="dropdown-item bg-secondary" href="#">Another action</a></li>
            <li><a style="background-color: red;"  class="dropdown-item bg-secondary" href="#">Something else here</a></li>
        </ul>
        </div>

    </div>
</template>
<script>
import axios from 'axios'

export default {
    async data() {
        try {
            return axios.get(`http://localhost:5000/players`)
        } catch (error) {
            console.error(error)
            return []
        }
    },
    name: 'SidebarItem'
}
</script>
<style lang="">
    
</style>