import Vue from 'vue';
import VueRouter from 'vue-router';

import Landing from '../pages/Landing.vue';
import SignupLogin from '../pages/SignupLogin.vue';
import Onboarding from '../pages/Onboarding.vue';
import Skills from '../pages/Skills.vue';

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
  {
    path: '/onboarding',
    name: 'onboarding',
    component: Onboarding
  },
  {
    path: '/skills',
    name: 'skills',
    component: Skills
  }
	
];

const router = new VueRouter({
  mode: 'history',
  routes
});
  
export default router;