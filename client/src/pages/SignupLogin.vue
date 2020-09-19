<template>
  <div class="container" id="container">
    <div class="form-container sign-up-container">
      <Login />
    </div>
    <div class="form-container sign-in-container">
      <Signup />
    </div>
    <div class="overlay-container">
      <div class="overlay">
        <div class="overlay-panel overlay-left">
          <SignupContain @shifted="movePanelLeft" />
        </div>
        <div class="overlay-panel overlay-right">
          <LoginContain @shifted="movePanelRight" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Signup from "../components/Signup"
import Login from "../components/Login"
import SignupContain from "../components/SignupContain"
import LoginContain from "../components/LoginContain"

export default {
  name: 'signuplogin',
  components:{
    Signup,
    SignupContain,
    Login,
    LoginContain
  },
  methods: {
    movePanelLeft() {
      document.getElementById('container').classList.remove('right-panel-active');
    },
    movePanelRight() {
      document.getElementById('container').classList.add('right-panel-active');
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Teko:wght@500&display=swap');

.container {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  position: relative;
  overflow: hidden;
  width: 80%;
  max-width: 100%;
  min-height: 480px;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}

.sign-in-container {
  display: flex;
  justify-content: center;
  left: 0;
  width: 50%;
  z-index: 2;
}

.sign-up-container {
  display: flex;
  justify-content: center;
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;  
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.overlay {
  background: #fff241;
  background: linear-gradient(to right, #ebd511, #d20afa) no-repeat 0 0 / cover;
  color: #fff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0) ;
  transition: transform 0.6s ease-in-out;
}

.overlay-panel {
  position: absolute;
  top: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
    align-items: center; 
  padding: 0 40px;
  height: 100%;
  width: 50%;
  text-align: center;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-right {
  right: 0;
  transform: translateX(0);
}

.overlay-left{ 
  transform: translateX(-20%);
}

/* Animation */

/* Move signin to the right */
.container.right-panel-active .sign-in-container{
  transform: translateX(100%);
}

/* Move overlay */
.container.right-panel-active .overlay-container{
  transform: translateX(-100%);
}

/* Sign up over Sign In */
.container.right-panel-active .sign-up-container{
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
}

/* Overlay Back to right */
.container.right-panel-active .overlay{
  transform: translateX(50%);
}

.container.right-panel-active .overlay-left{
  transform: translateX(0);
}

.container.right-panel-active .overlay-right{
  transform: translateX(20%);
}

</style>
