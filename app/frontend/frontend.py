import frontend_domain

from bottle import default_app, route, run, template

import os
import requests
import json

app = default_app()
app.config['backend.url'] = os.getenv('BACKEND_URL', 'http://localhost:8001')

@route('/')
def index():
    connector = BackendConnector(app.config['backend.url'])
    message = frontend_domain.the_message(connector)
    return '<html><h1>Welcome to master branch</h1><p>{}</p></html>'.format(message)

class BackendConnector:

    def __init__(self, backend_url):
        self.backend_url = backend_url

    def get_message(self):
        resp = requests.get(url=self.backend_url)
        j = resp.json()
        return j['message']

run(host='0.0.0.0', port=8000)

