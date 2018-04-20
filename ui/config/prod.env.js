'use strict'

const IAM_API_URL = 'http://localhost:8001'
const AUTH_API_URL = 'http://localhost:8002'
const LABS_API_URL = 'http://localhost:8003'

const LOGIN_ENDPOINT = AUTH_API_URL + '/auth'
const SIGNUP_ENDPOINT = IAM_API_URL + '/1/signup/'

module.exports = {
  NODE_ENV: '"production"',
  DEBUG_MODE: true,
  AUTH_API_URL: AUTH_API_URL,
  IAM_API_URL: IAM_API_URL,
  LABS_API_URL: LABS_API_URL,
  LOGIN_URL: '\'' + LOGIN_ENDPOINT + '\'',
  SIGNUP_URL: '\'' + SIGNUP_ENDPOINT + '\''
}
