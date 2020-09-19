<template>
  <div>
    <h1>resu.me</h1>
    <img src="../assets/logo.png" width="500px" length = "500px" class="imgstyle" alt="image">
    <StartButton />
  </div>
</template>

<script>

import StartButton from "../components/StartButton"
export default {
  name: 'landing',
  components:{
    StartButton
  },
}
</script>

<style scoped>
h1 {
  font-size: 50px;
  color: #2a2a2a;
}

.imgstyle {
  position: relative;
  top: -30px;
}
</style>
