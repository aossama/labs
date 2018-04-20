/**
 * Created by ahmed on 3/14/17.
 */

import Router from '../router'

export default {
  LOGIN_URL: process.env.LOGIN_URL,
  SIGNUP_URL: process.env.SIGNUP_URL,

  // User object will let us check authentication status
  user: {
    authenticated: false
  },

  // Send a request to the login URL and save the returned JWT
  login (context, creds, redirect) {
    context.$http.post(this.LOGIN_URL, creds).then(
      response => {
        localStorage.setItem('access_token', response.body.access_token)
        this.user.authenticated = true
        Router.go('Dashboard')
      }, response => {
        context.error = response.body
      })
  },

  signup (context, creds, redirect) {
    context.$http.post(this.SIGNUP_URL, creds).then(
      response => {
        // success callback
      }, response => {
        context.error = response.body
      })
  },

  // To log out, we just need to remove the token
  logout () {
    localStorage.removeItem('access_token')
    this.user.authenticated = false
  },

  checkAuth () {
    var jwt = localStorage.getItem('access_token')
    if (jwt) {
      this.user.authenticated = true
    } else {
      this.user.authenticated = false
    }
  },

  // The object to be passed as a header for authenticated requests
  getAuthHeader () {
    return {
      'Authorization': 'JWT ' + localStorage.getItem('access_token')
    }
  }
}
