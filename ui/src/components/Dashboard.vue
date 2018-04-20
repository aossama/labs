<template>
  <div class="dashboard">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import auth from '../auth'

export default {
  name: 'Dashboard',
  data () {
    return {
      msg: 'Dashboard',
      me: []
    }
  },
  methods: {
    whoAmI () {
      this.$http
        .get('http://127.0.0.1:8003/1/whoami', {
          headers: auth.getAuthHeader()
        }).then(
          response => {
            this.me = response.body
          }
        )
    }
  },
  mounted () {
    this.whoAmI()
  },
  route: {
    canActivate () {
      return auth.user.authenticated
    }
  }
}
</script>

<style scoped></style>
