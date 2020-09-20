import Vue from 'vue';
import VueRouter from 'vue-router';

import Landing from '../pages/Landing.vue';
import Onboarding from '../pages/Onboarding.vue';
import Skills from '../pages/Skills.vue';
import CoursesJobs from '../pages/CoursesJobs.vue';


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'landing',
    component: Landing
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
  },
  {
    path: '/results/:keyword/:location',
    name: 'results',
    component: CoursesJobs
  }

];

const router = new VueRouter({
  mode: 'history',
  routes
});

// router.beforeEach( (to, from, next) => {
//   if(to.name !== 'landing' && !Vue.$cookies.get('token')) next({ name: 'landing' })
//   else if(to.name === 'landing' && Vue.$cookies.get('token')) next({ name: 'skills' })
//   else next()
// })
  
export default router;