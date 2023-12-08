<template>
        <h1>task</h1>
</template>

<script>

export default {
    name: 'HeaderItem',
    props: {
        type: String
    }
}
</script>
<style scoped>
    h1 {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
</style>