from bottle import route, run, template
import my_domain

@route('/')
def index():
    message = my_domain.my_message()
    return '<html><h1>In Kubernetes dev-1</h1><p>{}</p></html>'.format(message)

run(host='0.0.0.0', port=8000)

