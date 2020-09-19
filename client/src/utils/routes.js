import Vue from 'vue';
import VueRouter from 'vue-router';

import Landing from '../pages/Landing.vue';
import SignupLogin from '../pages/SignupLogin.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'landing',
    component: Landing
  },
  {
    path: '/signuplogin',
    name: 'signuplogin',
    component: SignupLogin
	},
	
];

const router = new VueRouter({
  mode: 'history',
  routes
});
  
export default router;