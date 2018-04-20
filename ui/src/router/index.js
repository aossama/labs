import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard'
import Catalog from '@/components/Catalog'
import Lab from '@/components/Lab'
import Signup from '@/components/Signup'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/login', name: 'Login', component: Login },
    { path: '/signup', name: 'Signup', component: Signup },
    { path: '/dashboard', name: 'Dashboard', component: Dashboard },
    { path: '/catalog', name: 'Catalog', component: Catalog },
    { path: '/lab', name: 'Lab', component: Lab }
  ],
  mode: 'history'
})
