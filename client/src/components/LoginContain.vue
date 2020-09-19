<template>
  <div>
    <h1>Hello, Wanderer!</h1>
    <p>Enter your personal details and start journey with us</p>
    <button id="su" v-on:click="emitClick">Sign Up</button>
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
button{
    border-radius: 20px;
    border: 1px solid #f3f3f3;
    background: #23bebe;
    color: #fff;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: transform 80ms ease-in;
}

#su{
  background-color: rgb(235, 201, 13);
}
</style>