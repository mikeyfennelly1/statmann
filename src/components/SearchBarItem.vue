<template>
    <div class="container border border-dark">
        <input type="text" placeholder="Search Players" v-model="searchTerm" @input="searchPlayers()">
        <p>{{ searchTerm }}</p>
        <button onclick class="submit bg-dark">
            submit
        </button>
    </div>
</template>
<script>
import axios from 'axios'


export default {
    data() {
        return {
            searchTerm: ''
        }
    },
    methods: {
        async searchPlayers() {
            axios.get(`http://localhost:5000/videos/${this.searchTerm}`, {})
                .then(response => {
                    this.message = response.data.title
                    console.log(this.message)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    name: 'SearchBarItem'
}
</script>
<style>
    
</style>