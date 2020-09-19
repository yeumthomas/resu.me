<template>
    <div class="overlay-container">
            <div class="overlay">
                <div class="overlay-panel overlay-left">
                    <h1>Welcome Back!</h1>
                    <p>To Keep connected with us please login with your personal info</p>
                    <button class="ghost" id="signIn">Sign In</button>
                </div>
            </div>
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

 .overlay-left{ 
    transform: translateX(-20%);
}
</style>