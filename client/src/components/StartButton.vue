<template>
  <div>
    <button v-on:click="toSignupLogin">Begin</button>
  </div>
</template>

<script>
export default {
  name: 'StartButton',
  methods: {
    toSignupLogin() {
      this.$router.navigate('signuplogin')
    }
  }
}
</script>

<style scoped>
html {
  --BTNcolor-default: #FF006E;
  --BTNcolor-dark: #EE005D;
  --BTNcolor-text: #FFFFFF;
  --BTNradius: .5rem;
}

body {
  perspective: 500px;
}

button {
  position: relative;
  display: inline-block;
  border: none;
  padding: 0.5rem 1.5rem;
  border-radius: var(--BTNradius, .5rem);
  margin: 0;
  text-decoration: none;
  background: var(--BTNcolor-default, #ffb101);
  color: var(--BTNcolor-text, #2a2a2a);
  font-family: Avenir;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  text-align: center;
  transition: transform .15s ease;
  -webkit-appearance: none;
  -moz-appearance: none;
  z-index: 0;
  bottom: 0.8cm;
}

button::before,
button::after{
  content:"";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
  color: var(--BTNcolor-default, #666);
  border-radius: var(--BTNradius, .5rem);
  box-shadow: 0 0 0 0px;
  will-change: opacity;
  opacity: 0;
}

button::before {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  box-shadow: 0 0 0 5px;
  opacity: 0;
  z-index: -1;
  transition: opacity .15s ease;
  background: rgba(0,0,0,.1);
}

button::after {
  animation: pulse 2s infinite;
}

button:hover,
button:focus {
  background: var(--BTNcolor-dark, #2a2a2a);
  color: var(--BTNcolor-text, #ffb101);
}
button:hover {
  transform: translateZ(10px);
}

button:focus {
  outline: 0;
}
button::-moz-focus-inner {
  border: none;
}

button:focus::after,
button:active::after {
  animation-play-state: paused;
}

button:focus:not(:hover)::after,
button:active:not(:hover)::after {
  animation: none;
}

button:focus::before {
  opacity: .4;
}

button:active {
  transform: translateZ(-5px) translateY(2px);
}


@keyframes pulse {
  0%{
    opacity: .3;
    box-shadow: 0 0 0 0px var(--BTNcolor-default, #666);
  }
  70%, 100%{
    opacity: .0;
    box-shadow: 0 0 0 20px var(--BTNcolor-default, #666);
  }
}



/* Presentation styles */
body {
  display: grid;
  place-items: center;
  height: 100vh;
  background: #F0F0F0;
  margin: 0;
  perspective: 500px;
}
</style>