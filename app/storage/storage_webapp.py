from bottle import route, run, response
import storage_domain
import json

@route('/')
def index():
    data = storage_domain.get_data()
    result = {'data': data}
    response.content_type = 'application/json'
    return json.dumps(result)

run(host='0.0.0.0', port=8002)

