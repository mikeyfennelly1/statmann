<template>
    <div class="container border border-dark">
        <div>
            <h3>Search By:</h3>
            <input type="checkbox" name="activePlayers">
            <label for="activePlayers">Active Players</label>
            <br>
            <input type="checkbox" name="inactivePlayers">
            <label for="inactivePlayers">Inactive Players</label>
            <br>
            <input type="checkbox" name="allPlayers">
            <label for="allPlayers">All Players</label>
        </div>
        <input type="text" name="Search Players" placeholder="Search Players"  v-model="searchTermPlayer" @input="searchPlayers()">
        <input type="text" name="Search Teams" placeholder="Search Teams"  v-model="searchTermTeam" @input="searchTeams()">
        <ul style="background-color: black;" class="border bg-dark">
            <li style="font-size: xx-large; list-style-type: none;" class="bg-dark">Player: {{ playersFullName }}: {{playerID}}</li>
            <li style="font-size: xx-large; list-style-type: none;" class="bg-dark">Team: {{ teamFullName }}: {{teamID}}</li>
        </ul>
        <div>
            <button @click="getCareerStats()">Career Statistics</button><br>
            <button>Team Gamelog</button><br>
        </div>
        <div>
            <h1>stats</h1>
            <p> {{  careerStats }}</p>
        </div>
        <div>

        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    data() {
        return {
            searchTermPlayer: '',
            playersFullName: '',
            playerID: {type: Number},
            careerStats: '',
            playersPTS: '',

            searchTermTeam: '',
            teamFullName: '',
            teamID: {type: Number},
        }
    },
        methods: {
            async searchPlayers() {
            try {
                const players = await axios.get(`http://localhost:5000/players`, {
                    params: {
                    name: this.searchTermPlayer
                }
            })
            this.players = players.data[0]
            this.playersFullName = this.players["full_name"]
            this.playerID = this.players["id"]
            } catch (error) {
                console.error(error)
            }
        },
        async searchTeams() {
            try {
                const teams = await axios.get(`http://localhost:5000/teams`, {
                    params: {
                    name: this.searchTermTeam
                }
            })
            this.teams = teams.data[0]
            this.teamFullName = this.teams["full_name"]
            this.teamID = this.teams["id"]
            } catch (error) {
                console.error(error)
            }
        },
        async getCareerStats() {
            try {
                const careerStats = await axios.get(`http://localhost:5000/career_stats`, {
                    params: {
                        id: this.playerID
                    }
                })
                const resultSets = careerStats.data.resultSets
                // this.playersPTS = this.careerStats["parameters"].get("LeagueID")

                this.careerStats = {}

                resultSets.forEach(resultSet => {
                    const name = resultSet.name
                    const headers = resultSet.headers
                    const rowObjs = []

                    this.careerStats[name] = rowObjs
                    resultSet.rowSet.forEach(row => {
                        const rowObj = {}
                        row.forEach((value, index) => {
                            rowObj[headers[index]] = value
                            rowObjs.push(rowObj)
                        })
                    })
                });


                console.log(this.careerStats)
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