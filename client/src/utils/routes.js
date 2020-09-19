import Vue from 'vue';
import VueRouter from 'vue-router';

import Landing from '../pages/Landing.vue';
import Signup from '../pages/Signup.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'landing',
    component: Landing
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  }
];

const router = new VueRouter({
  mode: 'history',
  routes
});
  
export default router;