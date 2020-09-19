<template>
  <div class="justify-content-center">
    <h1>resu.me</h1>
    <img src="../assets/logo.png" width="500px" length = "500px" class="img-fluid my-1" alt="image">
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

</style>
