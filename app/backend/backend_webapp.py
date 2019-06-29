import backend_domain

from bottle import default_app, route, run, response
import os
import requests
import json

app = default_app()
app.config['storage.url'] = os.getenv('STORAGE_URL', 'http://localhost:8002')


@app.route('/')
def index():
    connector = StorageConnector(app.config['storage.url'])
    message = backend_domain.backend_message(connector)

    result = {'message': message}
    response.content_type = 'application/json'
    return json.dumps(result)


class StorageConnector:

    def __init__(self, storage_url):
        self.storage_url = storage_url

    def get_data(self):
        resp = requests.get(url=self.storage_url)
        j = resp.json()
        return j['data']




run(host='0.0.0.0', port=8001)

