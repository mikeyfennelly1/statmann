<template>
    <div class="container border border-dark">
        <input type="text" placeholder="Search Players" v-model="searchTerm" @input="searchPlayers()">
        <ul style="background-color: black;" class="border bg-dark">
            <li style="font-size: xx-large; list-style-type: none;" class="bg-dark">{{ playersFullName }}: {{playerID}}</li>
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
            playerID: {type: Number},
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
                this.playerID = this.players["id"]
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