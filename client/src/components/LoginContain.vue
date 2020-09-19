<template>
  <div>
    <h1>Been Here Before?</h1>
    <p>Enter your login information</p>
    <button id="su" v-on:click="emitClick">Sign In</button>
  </div>
</template>

<script>
export default {
  methods: {
    emitClick() {
      this.$emit('shifted')
    }
  }
}
</script>

<style scoped>
h1,p{
  color: #2a2a2a;
}
h1 {
  font-weight: bold;
}
button{
    border-radius: 20px;
    border: 1px solid #ffb101;
    color: #fff;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: transform 80ms ease-in;
}

#su{
  background-color: white;
  color: #2a2a2a;
}
</style>