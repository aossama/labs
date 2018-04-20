JWT_AUTH_URL_RULE = '/auth'
JWT_ALGORITHM = 'HS256'
# app.config['JWT_REQUIRED_CLAIMS'] = ['exp', 'iat', 'nbf', 'sub', 'iss']
JWT_REQUIRED_CLAIMS = ['exp', 'iat', 'nbf']
