<template>
     <div class="form-container sign-up-container">
            <form action="#">
                <h1>Create Account</h1>
                
                <span>or use your email for registration</span>
                <input type="text" placeholder="Name"/>
                <input type="email" placeholder="Email"/>
                <input type="password" placeholder="Password"/>
                <button class="su" >Sign Up</button>
            </form>
        </div>
</template>

<script>


export default {
  name: 'login',
  components:{
        
  },
}
</script>

<style scoped>

h1{
    font-weight: bold;
    letter-spacing: 0.8px;
    margin: 0;
}
p{
    font-size: 18px;
    font-weight: 100;
    line-height: 20px;
    letter-spacing: 0.5px;
    margin: 20px 0 30px;
}
span{
    font-size: 16px;
    letter-spacing: 0.8px;
}
a{
    color: #333;
    font-size: 16px;
    letter-spacing: 0.5px;
    text-decoration: none;
    margin: 15px 0;
}
.container{
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
    position: relative;
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 480px;
}
.form-container form{
    background: #fff;
    display: flex;
    flex-direction: column;
    padding: 0 50px;
    height: 100%;
    justify-content: center;
    text-align: center;
    align-items: center;
}
.social-container{
    margin: 20px 0;
}
.social-container a{
    border: 1px solid #ddd;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin: 0 5px;
    height: 40px;
    width: 40px;
}
.form-container input{
    background: #eee;
    border: none;
    padding: 12px 15px;
    margin: 8px 0;
    width: 100%;
}
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
button:active{
    transform: scale(0.95);
}
button:focus{
    outline: none;
}
button.ghost{
    background: transparent;
    border-color: #fff;
}
.sign-up-container{
    left: 0;
    width: 50%;
    opacity: 0;
    z-index: 1;  
}
.form-container{
    position: absolute;
    top: 0;
    height: 100%;
    transition: all 0.6s ease-in-out;
}

</style>