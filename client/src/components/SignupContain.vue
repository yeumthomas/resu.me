<template>
  <div>
    <h1>Welcome Back!</h1>
    <p>To Keep connected with us please login with your personal info</p>
    <button id="si" v-on:click="emitClick">Sign In</button>
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

#si{
  background-color: rgb(235, 4, 216);
}
</style>