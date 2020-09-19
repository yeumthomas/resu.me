import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'

import router from './utils/routes.js';

Vue.config.productionTip = false;

Vue.use(router);
Vue.use(ElementUI);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
