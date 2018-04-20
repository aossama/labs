import Vue from 'vue'
import App from './App'
import router from './router'

import VueResource from 'vue-resource'
import auth from './auth'

Vue.config.productionTip = false

Vue.use(VueResource)

Vue.http.headers.common['Authorization'] = 'JWT ' + localStorage.getItem('access_token')

// Check the user's auth status when the app starts
auth.checkAuth()

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
