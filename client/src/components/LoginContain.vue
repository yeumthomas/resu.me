<template>
  <div>
    <h1>Been Here Before?</h1>
    <p>Enter your login information</p>
    <button id="su" v-on:click="emitClick">sign in</button>
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
    border: 1px solid #fff241;
    color: #fff;
    font-size: 20px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: .05rem;
    transition: transform 80ms ease-in;
}

#su{
  background-color: white;
  color: #2a2a2a;
}
</style>