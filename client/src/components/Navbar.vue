<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand><img src="../assets/img/logo-bee.png" class="img-fluid my-1" style="width:100px;height:100px;" alt="image"></b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Some Link</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <Switch />
        <b-nav-item right>
          View Profile
        </b-nav-item>
        <b-nav-item right>
          Log Out
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
    

<script>
import Switch from "./Switch"
export default {
  Switch
}
</script>

<style scoped>
b-navbar{
  background: #ffffff;
}
</style>