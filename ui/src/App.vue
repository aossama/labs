<template>
  <div id="app">
    <nav>
      <div class="container">
        <ul id="navlist">
          <router-link tag="li" to="/"><a>Home</a></router-link>
          <router-link tag="li" to="/signup" v-if="!user.authenticated"><a>Signup</a></router-link>
          <router-link tag="li" to="/login" v-if="!user.authenticated"><a>Login</a></router-link>

          <router-link tag="li" to="/dashboard" v-if="user.authenticated"><a>Dashboard</a></router-link>
          <router-link tag="li" to="/catalog" v-if="user.authenticated"><a>Catalog</a></router-link>
          <router-link tag="li" to="/lab" v-if="user.authenticated"><a>Lab</a></router-link>

          <li v-if="user.authenticated"><a router-link="'login'" @click="logout()">Logout</a></li>
        </ul>
      </div>
    </nav>

    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import auth from './auth'

export default {
  name: 'app',
  data () {
    return {
      user: auth.user
    }
  },
  methods: {
    logout () {
      auth.logout()
    }
  }
}
</script>

<style>
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  #navlist {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  #navlist li {
    display: inline;
  }
  .container {
    width: 900px;
    margin: 10px auto;
  }
</style>
