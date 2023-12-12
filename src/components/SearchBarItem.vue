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
            try {
                const players = await axios.get(`http://localhost:5000/players`, {
                    params: {
                        name: this.searchTerm
                    }
                })
                console.log(players)
            } catch (error) {
                console.error(error)
            }
        }
    },
    name: 'SearchBarItem'
}
</script>
<style>
    
</style>