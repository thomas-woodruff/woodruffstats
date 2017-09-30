import urllib.parse
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import read_credentials

# application credentials
credentials = read_credentials.read_credentials()

client_id = credentials['key']
client_secret = credentials['secret']



# As a convenience, localhost.mapmyapi.com redirects to localhost.
redirect_uri = 'http://localhost.mapmyapi.com:12345/callback'
redirect_uri_escaped = 'http%3A%2F%2Flocalhost.mapmyapi.com%3A12345%2Fcallback'
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

print('server_address:', server_address)

# NOTE: Don't go to the web browser just yet...
webbrowser.open(authorize_url)

# Start our web server. handle_request() will block until a request comes in.
httpd = HTTPServer(server_address, AuthorizationHandler)
print('Now waiting for the user to authorize the application...')
httpd.handle_request()

# At this point a request has been handled. Let's parse its URL.
# httpd.server_close()
# callback_url = urllib.parse.urlparse(httpd.path)
# authorize_code = urllib.parse.parse_qs(callback_url.query)['code'][0]


# print('Got an authorize code:', authorize_code)

# access_token_url = 'https://api.mapmyfitness.com/v7.1/oauth2/access_token/'
# access_token_data = {'grant_type': 'authorization_code',
#                      'client_id': client_id,
#                      'client_secret': client_secret,
#                      'code': authorize_code}

# response = requests.post(url=access_token_url,
#                          data=access_token_data,
#                          headers={'Api-Key': client_id})

# print('Request details:')
# print('Content-Type:', response.request.headers['Content-Type'])
# print('Request body:', response.request.body)


# # retrieve the access_token from the response
# try:
#     access_token = response.json()
#     print('Got an access token:', access_token)
# except:
#     print('Did not get JSON. Here is the response and content:')
#     print(response)
#     print(response.content)


# # Use the access token to request a resource on behalf of the user
# activity_type_url = 'https://api.ua.com/v7.1/activity_type/'
# test_response = requests.get(url=activity_type_url, verify=False,
#                         headers={'api-key': client_id, 'authorization': 'Bearer %s' % access_token['access_token']})


# print(test_response.json())



