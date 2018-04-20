<template>
  <div class="col-sm-4 col-sm-offset-4">
    <h1>Sign Up</h1>
    <p>Sign up for a free account</p>
    <div class="alert alert-danger" v-if="error">
      <p>{{ error }}</p>
    </div>
    <div class="form-group">
      <input type="text" class="form-control" placeholder="Enter your Firstname" v-model="credentials.first_name" >
    </div>
    <div class="form-group">
      <input type="text" class="form-control" placeholder="Enter your Lastname" v-model="credentials.last_name" >
    </div>
    <div class="form-group">
      <input type="text" class="form-control" placeholder="Enter your username" v-model="credentials.username" >
    </div>
    <div class="form-group">
      <input type="text" class="form-control" placeholder="Enter your email" v-model="credentials.email" >
    </div>
    <div class="form-group">
      <input type="text" class="form-control" placeholder="Enter your mobile" v-model="credentials.mobile" >
    </div>
    <div class="form-group">
      <input type="password" class="form-control" placeholder="Enter your password" v-model="credentials.password" >
    </div>
    <button class="btn btn-primary" @click="submit()">Access</button>
  </div>
</template>

<script>
import auth from '../auth'
export default {
  name: 'Signup',
  data () {
    return {
      credentials: {
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        mobile: '',
        password: ''
      },
      error: ''
    }
  },
  methods: {
    submit () {
      var credentials = {
        first_name: this.credentials.first_name,
        last_name: this.credentials.last_name,
        username: this.credentials.username,
        email: this.credentials.email,
        mobile: this.credentials.mobile,
        password: this.credentials.password
      }
      auth.signup(this, credentials, 'Dashboard')
    }
  }
}
</script>

<style scoped></style>
