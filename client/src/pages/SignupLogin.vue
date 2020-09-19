<template>
    <div>
     <Signup />   
     <Login />
     <SignupContain />
     <LoginContain />
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
  }
  
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Teko:wght@500&display=swap');
*{
    box-sizing: border-box;
}

body{
    background: #86235a;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: -20px 0 50px;
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
