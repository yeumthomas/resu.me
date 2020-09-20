<template>
  <div class="container-fluid d-flex justify-content-center align-items-center">
    <div class="justify-content-center">
      <h1>resu.<span style="color: #32afc7">me</span></h1>
      <img src="../assets/img/logo-bee.png" class="img-fluid my-1" alt="image">
      <StartButton @clicked="displayOverlay" />
    </div>
    <div class="dark-overlay d-flex align-items-center" id="login">
      <SignupLogin @close="closeOverlay" />
    </div>
    <div id="diamond-yellow">
    </div>
    <div id="diamond-blue">
    </div>
  </div>
</template>

<script>
import StartButton from "../components/StartButton";
import SignupLogin from "../components/SignupLogin";

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

#diamond-yellow {
  position: absolute;
  background: rgb(255,177,1, .3);
  height: 120vh;
  text-align: center;
  transform:rotate(45deg);
	width: 120vh;
  z-index: -1;
}

#diamond-blue {
  position: absolute;
  border: 1.25rem solid #a2dce7;
  height: 130vh;
  text-align: center;
  transform:rotate(45deg);
	width: 130vh;
  z-index: -1;
}
</style>
