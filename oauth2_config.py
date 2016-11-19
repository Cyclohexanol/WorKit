class oauth2_config:
    scopes = None
    client_id = None
    client_secret = None
    redirect_uri = None

    def __init__(self, scopes, client_id, client_secret, redirect_uri):
        self.scopes = scopes
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
