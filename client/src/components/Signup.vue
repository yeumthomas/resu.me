<template>
  <form>
    <h1 class="font-weight-bold">Create Account</h1>
    <span>Use your email for registration</span>
    <input type="text" placeholder="Name" v-model="name" />
    <input type="email" placeholder="Email" v-model="email" />
    <input type="password" placeholder="Password" v-model="password" />
    <button type="button" class="btn" v-on:click="sendSignupRequest">Sign Up</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      password: ''
    }
  },
  methods: {
    sendSignupRequest() {
      if(this.name.length > 0 && this.email.length > 0 && this.password.length > 0) {
        axios({
          method: 'post',
          url: 'http://localhost:3000/api/v1/auth/signup',
          data: {
            email: this.email,
            password: this.password,
            name: this.name,
            classes: []
          }
        }).then( (response) => {
          this.$cookies.set('token', response.data.token)
          this.$router.push('onboarding')
        })
      }
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