<template>
  <form>
    <h1 class="font-weight-bold">Create Account</h1>
    <span>Use your email for registration</span>
    <input type="text" placeholder="Name" v-model="name" />
    <input type="email" placeholder="Email" v-model="email" />
    <input type="password" placeholder="Password" v-model="password" />
    <button type="button" class="btn" v-on:click="sendSignupRequest">Sign Up</button>
    <b-alert show variant="danger" class="mt-2" v-if="error">{{ error }}</b-alert>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      password: '',
      error: ''
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
            name: this.name
          }
        }).then( (response) => {
          this.$cookies.set('token', response.data.token)
          this.$router.push('onboarding')
        }).catch( () => {
          this.error = 'Invalid email, password, or name field'
        })
      } else {
        this.error = 'Email, password, or name empty'
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
  color: #2a2a2a;
  background: #fff241;
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