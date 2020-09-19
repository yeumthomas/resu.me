<template>
    <div>
        <h1>resu.me</h1>
        <img src="../assets/logo.png" width="500px" length = "500px">
        <start_button/>
    </div>
</template>

<script>

import start_button from "../components/start_button"
export default {
  name: 'landing',
  components:{
        start_button
  },
}
</script>

<style scoped>
h1 {
  font-size: 50px;
}
</style>
