<template>
    <div class="overlay-panel overlay-right">
        <h1>Hello, Wanderer!</h1>
        <p>Enter your personal details and start journey with us</p>
        <button class="ghost" id="signUp">Sign Up</button>
    </div>
</template>

<style scoped>
.si{
    background-color: rgb(235, 4, 216);
}
.su{
    background-color: rgb(235, 201, 13);
}



.overlay-container{
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: transform 0.6s ease-in-out;
    z-index: 100;
}
.overlay{
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
.overlay-panel{
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

.overlay-right{
    right: 0;
    transform: translateX(0);
}
 .overlay-left{ 
    transform: translateX(-20%);
}
</style>