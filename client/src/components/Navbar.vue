<template>
  <div class="container mt-5">
    <b-navbar toggleable="lg" type="light" variant="faded" id="navbar">
      <b-navbar-brand class="mt-3"><h1>resu.<span style="color: #32afc7">me</span></h1></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item class="nav-item" right>
            <router-link class="nav-link" to="/onboarding"> Refill Form </router-link>
          </b-nav-item>
          <b-nav-item class="nav-item" right>
            <router-link class="nav-link" to="/skills"> Browse Interests </router-link>
          </b-nav-item>
          <b-nav-item class="nav-item" right>
            <router-link class="nav-link" to="/profile"> View Profile </router-link>
          </b-nav-item>
          <b-nav-item class="nav-item" right>
            <button class="btn btn-danger" v-on:click="logout()"> Log Out </button>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
    

<script>
export default {
  methods: {
    logout() {
      this.$cookies.remove('token')
      this.$router.push({ name: 'landing' })
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Kufam:wght@700&display=swap');

h1 {
  font-size: 4rem;
  font-family: 'Kufam', cursive;
  color: #2a2a2a;
}

#navbar {
  background: #fafafa;
}

b-navbar{
  background: #ffffff;
}

.nav-item {
  margin: 0rem 1rem;
}

.nav-link {
  text-decoration: none;
  color: #000;
}
</style>