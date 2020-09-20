<template>
  <div class="container-fluid d-flex justify-content-center align-items-center">
    <div class="justify-content-center">
      <h1>resu.<span style="color: #ffb101">me</span></h1>
      <img src="../assets/img/logo-bee.png" class="img-fluid my-1" alt="image">
      <StartButton @clicked="displayOverlay" />
    </div>
    <div class="dark-overlay d-flex align-items-center" id="login">
      <SignupLogin @close="closeOverlay" />
    </div>
  </div>
</template>

<script>
import StartButton from "../components/StartButton";
import SignupLogin from "./SignupLogin";

export default {
  name: 'landing',
  components:{
    StartButton,
    SignupLogin
  },
  methods: {
    displayOverlay() {
      document.getElementById('login').style.visibility = 'visible';
      document.getElementById('login').style.opacity = 1;
    },
    closeOverlay() {
      document.getElementById('login').style.visibility = 'hidden';
      document.getElementById('login').style.opacity = 0;
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Kufam:wght@700&display=swap');

.dark-overlay {
  visibility: hidden;
  opacity: 0;
  transition: visibility 0s, opacity 0.2s linear;
  background-color: rgb(0,0,0,.7);
  position: absolute;
  width: 100vw;
  height: 100vh;
}

h1 {
  font-size: 4rem;
  font-family: 'Kufam', cursive;
  color: #2a2a2a;
}

</style>
