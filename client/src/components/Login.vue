<template>
  <form>
    <h1 class="font-weight-bold">Sign In</h1>
    <span>Log in with your email</span>
    <input type="email" placeholder="Email" v-model="email" />
    <input type="password" placeholder="Password" v-model="password" />
    <a href="" class="my-2 text-muted">Forgot Password</a>
    <button type="button" class="btn" v-on:click="sendLoginRequest">Sign In</button>
    <b-alert show variant="danger" class="mt-2" v-if="error">{{ error }}</b-alert>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    sendLoginRequest() {
      console.log('asdf')
      if(this.email.length > 0 && this.password.length > 0) {
        axios({
          method: 'post',
          url: 'http://localhost:3000/api/v1/auth/login',
          data: {
            email: this.email,
            password: this.password
          }
        }).then( (response) => {
          this.$cookies.set('token', response.data.token)
          this.$router.push({ name: 'skills'})
        }).catch( () => {
          this.error = 'Incorrect email or password'
        })
      } else {
        this.error = 'Email or password field empty'
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
  color: #2a2a2a;
  text-decoration: none;
}

.btn {
  color: #2a2a2a;
  background: #a2dce7;
  border: 1px solid #f3f3f3;
  border-radius: 20px;
  padding: .75rem 2rem;
  text-transform: lowercase;
  letter-spacing: .05rem;
  font-size: 20px;
  font-weight: bold;
}

.btn:hover {
  background: #32afc7;
  color: #2a2a2a;
}
</style>