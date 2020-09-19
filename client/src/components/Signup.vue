<template>
  <form>
    <h1 class="font-weight-bold">Create Account</h1>
    <span>Use your email for registration</span>
    <input type="text" placeholder="Name"/>
    <input type="email" placeholder="Email"/>
    <input type="password" placeholder="Password"/>
    <button class="btn">Sign Up</button>
  </form>
</template>

<script>
export default {
}
</script>

<style scoped>
form {
  background: #fff;
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 50%;
  justify-content: center;
  text-align: center;
  align-items: center;
}

input {
  background: #eee;
  border: none;
  padding: .5rem;
  margin: .5rem;
  width: 75%;
  border-radius: 12px;
}

h1, span, a {
  letter-spacing: .1rem;
  margin: 0;
  color: #000;
  text-decoration: none;
}

.btn {
  color: white;
  background: #23bebe;
  border: 1px solid #f3f3f3;
  border-radius: 20px;
  padding: .75rem 2rem;
  text-transform: uppercase;
  letter-spacing: .1rem;
  font-size: .8rem;
  font-weight: bold;
}

.btn:hover {
  background: #16a9a9;
}
</style>