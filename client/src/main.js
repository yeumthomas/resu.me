import Vue from 'vue';
import App from './App.vue';
import ElementUI from 'element-ui';
import { BootstrapVue } from 'bootstrap-vue';
import VueCookies from 'vue-cookies';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './utils/routes.js';


Vue.config.productionTip = false;

Vue.use(router);
Vue.use(ElementUI);
Vue.use(BootstrapVue);
Vue.use(VueCookies);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
