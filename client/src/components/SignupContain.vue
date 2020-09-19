<template>
  <div>
    <h1>New Here?</h1>
    <p>Create an account</p>
    <button id="si" v-on:click="emitClick">Sign Up</button>
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
    color: #2a2a2a;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: transform 80ms ease-in;
}

#si{
  background-color: #ffffff;
  color: #2a2a2a;
}
</style>