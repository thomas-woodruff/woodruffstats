import urllib.parse
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import woodruffstats.read_credentials as read_credentials


def get_access_token(credentials):
    # application credentials
    client_id = credentials['key']
    client_secret = credentials['secret']

    # # As a convenience, localhost.mapmyapi.com redirects to localhost.
    redirect_uri = 'http://localhost.mapmyapi.com:12345/callback'
    authorize_url = 'https://api.ua.com/v7.1/oauth2/authorize/?' \
                    'client_id={0}&response_type=code&redirect_uri={1}'.format(client_id, redirect_uri)

    # Set up a basic handler for the redirect issued by the MapMyFitness
    # authorize page. For any GET request, it simply returns a 200.
    # When run interactively, the request's URL will be printed out.
    class AuthorizationHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.server.path = self.path

    parsed_redirect_uri = urllib.parse.urlparse(redirect_uri)
    server_address = parsed_redirect_uri.hostname, parsed_redirect_uri.port

    # NOTE: Don't go to the web browser just yet...
    webbrowser.open(authorize_url)

    # Start our web server. handle_request() will block until a request comes in.
    httpd = HTTPServer(server_address, AuthorizationHandler)
    httpd.handle_request()
    # At this point a request has been handled. Let's parse its URL.
    httpd.server_close()
    callback_url = urllib.parse.urlparse(httpd.path)
    authorize_code = urllib.parse.parse_qs(callback_url.query)['code'][0]

    # retrieve access token using authorize_code
    access_token_url = 'https://api.mapmyfitness.com/v7.1/oauth2/access_token/'
    access_token_data = {'grant_type': 'authorization_code',
                         'client_id': client_id,
                         'client_secret': client_secret,
                         'code': authorize_code}

    response = requests.post(url=access_token_url,
                             data=access_token_data,
                             headers={'Api-Key': client_id})
    
    try:
        # add logic around including expiration time
        return response.json()
    except:
        print('Did not get JSON')


def refresh_token(credentials, access_token):
    # application credentials
    client_id = credentials['key']
    client_secret = credentials['secret']

    # Refresh a client's credentials to prevent expiration
    refresh_token_url = 'https://api.ua.com/v7.1/oauth2/access_token/'
    refresh_token_data = {'grant_type': 'refresh_token',
                          'client_id': client_id,
                          'client_secret': client_secret,
                          'refresh_token': access_token['refresh_token']}

    response = requests.post(url=refresh_token_url, data=refresh_token_data,
                             headers={'api-key': client_id,
                             'authorization': 'Bearer %s' % access_token['access_token']})

    try:
        # add logic around including expiration time
        return response.json()
    except:
        print('Did not get JSON')


def construct_auth_headers(client_id, access_token):
    
    # add logic around refreshing token

    return {'api-key': client_id, 'authorization': 'Bearer %s' % access_token['access_token']}


def get_user_id(access_token):
    return access_token['user_id']
