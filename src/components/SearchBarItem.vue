<template>
    <div class="container border border-dark">
        <input type="text" placeholder="Search Players" v-model="searchTerm" @input="searchPlayers()">
        <p>{{ searchTerm }}</p>
        <ul>
            <li >{{ playersFullName }}</li>
        </ul>
    </div>
</template>
<script>
import axios from 'axios'


export default {
    data() {
        return {
            searchTerm: '',
            playersFullName: '',
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
                this.players = players.data[0]
                this.playersFullName = this.players["full_name"]
                console.log(this.playersFullName)
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