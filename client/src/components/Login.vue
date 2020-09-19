<template>
  <form>
    <h1 class="font-weight-bold">Sign In</h1>
    <span>Log in with your email</span>
    <input type="email" placeholder="Email"/>
    <input type="password" placeholder="Password"/>
    <a href="" class="my-2 text-muted">Forgot Password</a>
    <button class="btn btn-outline-primary" v-on:click="toSkills">SIGN IN</button>
  </form>
</template>

<script>
export default {
  name: 'Login',
  methods: {
    toSkills() {
      this.$router.push('skills')
    }
  }
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
  color: #2a2a2a;
  text-decoration: none;
}

.btn {
  color: #2a2a2a;
  background: #ffb101;
  border: 1px solid #f3f3f3;
  border-radius: 20px;
  padding: .75rem 2rem;
  text-transform: uppercase;
  letter-spacing: .1rem;
  font-size: .8rem;
  font-weight: bold;
}

.btn:hover {
  background: #2a2a2a;
  color: #ffb101;
}
</style>