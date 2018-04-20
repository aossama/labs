<template>
  <div class="catalog">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import auth from '@/auth'

export default {
  name: 'Catalog',
  data () {
    return {
      msg: 'Catalog'
    }
  },
  methods: {
    catalog () {
      this.$http.get('http://127.0.0.1:8003/1/catalog/', {
        headers: auth.getAuthHeader()
      }).then(
        response => {
          this.catalog = response.body
        }
      )
    }
  },
  mounted () {
    this.catalog()
  },
  route: {
    canActivate () {
      return auth.user.authenticated
    }
  }
}
</script>

<style scoped>

</style>
